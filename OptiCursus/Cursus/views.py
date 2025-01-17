from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpRequest, Http404
from django.urls import reverse
import os
import requests
from bs4 import BeautifulSoup
from langchain.llms import Cohere
from langchain.chains import LLMChain, ConversationChain, RetrievalQA, ConversationalRetrievalChain
from langchain.memory import ConversationSummaryMemory, ConversationBufferMemory, ChatMessageHistory
from langchain.agents import initialize_agent, Tool
from langchain.document_loaders import PyPDFLoader, TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import faiss, chroma, pinecone



cohere_api_token = os.environ.get("COHERE_API_TOKEN")
llm = Cohere(cohere_api_key=cohere_api_token)

def scrap_web(url: str): #https://cataloguelm.campusfrance.org/master/
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

tools = Tool(name="Web Scraper", func=scrap_web, description="Useful for scrapping cursus programs")


scrapper_agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",  # Agent type
    verbose=True  # Print detailed logs
)


# Create your views here.



# def quality_scale(self):
#     pass

# def tuition_fee_scale(self):
#     pass

# def living_cost_scale(self):
#     pass








# masters_programs = [
#     {"name": "Program A", "university": "Uni 1", "quality": 8, "tuition_fee": 5000, 
#      "living_cost": 12000, "domain": "AI", "type": "Research", "eligibility_score": 75},
#     {"name": "Program B", "university": "Uni 2", "quality": 7, "tuition_fee": 3000, 
#      "living_cost": 10000, "domain": "Data Science", "type": "Professional", "eligibility_score": 85},
#     # Add more programs...
# ]



# def calculate_program_score(user_profile, program, weights):
#     # weights: dict of weights for factors like quality, cost, etc.
#     eligibility = calculate_eligibility_score(user_profile, program)
#     cost = program["tuition_fee"] + program["living_cost"]
#     if cost > user_profile["budget"]:
#         return 0  # Filter out programs exceeding the budget
#     return (weights["quality"] * program["quality"] + 
#             weights["eligibility"] * eligibility +
#             weights["cost"] * (1 / cost))  # Lower cost = higher score


#  Program Selection
# Use multi-factor optimization to rank programs.
# Apply Gini Index or diversity check to reduce redundancy.
# Incorporate the Barbell Strategy by separating high-risk and low-risk programs.


# def recommend_programs(user_profile, programs, weights, max_choices=7):
#     scores = []
#     for program in programs:
#         score = calculate_program_score(user_profile, program, weights)
#         if score > 0:
#             scores.append((program, score))
    
#     # Sort programs by score (descending)
#     scores.sort(key=lambda x: x[1], reverse=True)
    
#     # Apply Barbell Strategy
#     low_risk = [p for p in scores if p[0]["eligibility_score"] > 70][:max_choices//2]
#     high_risk = [p for p in scores if p[0]["eligibility_score"] <= 70][:max_choices//2]
    
#     return low_risk + high_risk
