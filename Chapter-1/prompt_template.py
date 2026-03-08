from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import GoogleGenerativeAI
prompt=PromptTemplate(input_variables=["country"],template="What is the capital of {country}?")
parser=StrOutputParser()
llm =GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.9, max_tokens=2048,api_key="AIzaSyA236m4BbMA8vPV93p7dta6YbqA4FV5agU")