from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, AutoModelForSeq2SeqLM
from langchain.llms import HuggingFacePipeline 
from langchain.chains import LLMChain

# tokenizer = AutoTokenizer.from_pretrained("decapoda-research/llama-3-70b-instruct-titan-0.1")
# model = AutoModelForCausalLM.from_pretrained("decapoda-research/llama-3-70b-instruct-titan-0.1")


# model = AutoModelForCausalLM.from_pretrained("google/flan-t5-large")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")

tokenizer.pad_token = tokenizer.eos_token

hf_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device="cpu",  # Use GPU/cuda if available
    max_length=100,
    truncation = True, 
    temperature=0.7,
    do_sample = True
)

llm = HuggingFacePipeline(pipeline=hf_pipeline)


# Define a prompt template
prompt_template = PromptTemplate(
    input_variables=["input_text"],
    template="You are a helpful AI assistant. Respond to the following: {input_text}"
)

# Create an LLMChain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Run the chain
input_text = "Explain the concept of quantum computing in simple terms."
response = chain.run(input_text)

print(response)
