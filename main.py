from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_community.llms import GPT4All

load_dotenv()  #loads environment variables from .env file
# llm=ChatOpenAI(model="gpt-4", temperature=0.7) #for OpenAI LLM
llm = GPT4All(
    model="C:/Users/shail/gpt4all-models/ggml-gpt4all-j-v1.3-groovy.bin"
    )  #for local GPT4All LLM
# llm2=ChatAnthropic(model="claude-2", temperature=0.7) #for Anthropic LLM

# response=llm2.invoke("What is the capital of France?") #invoke method to get response from CLAUDE LLM
# print(response)

response = llm.invoke("What is the capital of France?")
print(response)