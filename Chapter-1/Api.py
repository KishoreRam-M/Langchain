

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

prompt = ChatPromptTemplate.from_messages(
    [("system","you are a helpful assistant that answers questions about the world"),
     ("human","What is the capital of {country}?")],
)
parser=StrOutputParser()
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.9, max_tokens=2048,api_key="AIzaSyA236m4BbMA8vPV93p7dta6YbqA4FV5agU")

chain=prompt|llm|parser

response =chain.invoke({"country":"INDIA"})
print(response)