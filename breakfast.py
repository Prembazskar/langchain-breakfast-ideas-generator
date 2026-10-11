
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load API key from the .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing. Check your .env file.")

# Initialize LangChain ChatOpenAI
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key=api_key
)

# Ask for exactly 5 healthy breakfast ideas
prompt = """
Suggest exactly 5 healthy breakfast ideas.
Format requirements:
- Number the ideas from 1 to 5.
- Write each idea on one line.
- Do not include any preamble or introduction.
- Do not include a conclusion.
"""

# Invoke the model and print only the reply text
response = llm.invoke(prompt)
print(response.content)
