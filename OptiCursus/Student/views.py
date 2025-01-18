from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.http import Http404, HttpRequest, request
from .models import Student
import os
import requests
from bs4 import BeautifulSoup
import settings
from langchain.llms import Cohere 
from langchain.chains import LLMChain, RetrievalQA, ConversationChain
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
#RAG LangChain libs
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.agents import initialize_agent, AgentExecutor, Tool, load_tools

DB_FAISS_PATH = os.path.abspath(os.path.join('vectorstore', 'db_faiss'))

# Initialize the LLM
cohere_api_token = os.environ.get("COHERE_API_TOKEN")

llm = Cohere(cohere_api_key=cohere_api_token)

message_history = ChatMessageHistory()

memory = ConversationBufferMemory(
    memory_key="chat_history",
    input_key = "message",
    output_key="answer",
    chat_memory=message_history,
    return_messages=True,
)

SK = 0

# Create vector database
def create_vector_db(DATA_PATH):
    # Load documents from PDF files
    loader = DirectoryLoader(DATA_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    
    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
        
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/multi-qa-mpnet-base-dot-v1',
                                       model_kwargs={'device': 'cpu'})

    db = FAISS.from_documents(texts, embeddings)
    db.save_local(DB_FAISS_PATH)


def RetrieveProfile():
    # Retrieve vector database
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/multi-qa-mpnet-base-dot-v1",
                                       model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    #Retrieval QA Chain
    qa = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type='stuff',
                                       retriever=db.as_retriever(search_kwargs={'k': 2}),
                                       chain_type_kwargs={'prompt':SK},
                                       return_source_documents=True,
                                       )
    response = qa("Extract skills from the CV as well as their mastery level by the user.")
    result = response["result"]  # Access the result
    return result


# Create your views here.

upload_dir = os.path.join(settings.BASE_DIR, "Uploads")
os.makedirs(upload_dir, exist_ok=True)  # Create directory if it doesn't exist


student = Student.objects.create()

def Preferences(request):
    global student
    if request.method == "POST":
        form = request.POST
        form_dict = form.dict()
        
        student.Domain = form_dict.get("favorite_domain")
        student.CareerGoals = form_dict.get("career_goal")
        student.Level = form_dict.get("cursus_level")
        student.save()
        return redirect("/Data")
    
    return render(request, "templates/data.html")
        
        
def CVHandler(request):
    global student
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/multi-qa-mpnet-base-dot-v1",
                                       model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    #Retrieval QA Chain
    qa = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type='stuff',
                                       retriever=db.as_retriever(search_kwargs={'k': 2}),
                                       chain_type_kwargs={'prompt':SK},
                                       return_source_documents=True,
                                       )
    if request.method == "POST":
        uploadedfile = request.FILES['CV']
        student.CV = uploadedfile
        student.save()                    
        filepath = os.path.join(upload_dir, uploadedfile.name)
        with open(filepath, "w") as buffer:
             for chunk in uploadedfile.chunks():
                    buffer.write(chunk)

        response = qa("Extract skills from the CV as well as their mastery level by the user.")
        result = response["result"]  # Access the result
        return result
    
    return render(request, "templates/data.html")
    
def WebScrapper(request): #https://cataloguelm.campusfrance.org/master/
    if request.method == "POST":
        url = request.POST
    try:        
        response = requests.get(url)
        response.raise_for_status()
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        # Extract the title
        title = soup.title.string if soup.title else "No Title"
        # Extract the first 200 characters of text
        text = soup.get_text()[:200] + "..." if soup.get_text() else "No Text"
        return f"Title: {title}\nText Snippet: {text}"
    except Exception as e: 
        return f"error {e}"

tools = Tool(name="Web Scraper", func=WebScrapper, description="Useful for scrapping cursus programs")


scrapper_agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",  # Agent type
    verbose=True  # Print detailed logs
)




# User Profile Input
# Gather user information to evaluate eligibility.


def calculate_eligibility_score(user_profile, program):
    gpa_weight = 0.6
    exp_weight = 0.4
    gpa_score = (user_profile["gpa"] / 4.0) * 100
    exp_score = (user_profile["experience"] / 5) * 100  # Assume 5 years max experience
    return gpa_weight * gpa_score + exp_weight * exp_score

