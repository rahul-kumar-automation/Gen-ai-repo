from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq

load_dotenv()

loader = WebBaseLoader("https://console.groq.com/docs/overview")
docs = loader.load()

print(docs[0].page_content[:500])

# Send to Groq
llm = ChatGroq(model="qwen/qwen3.8-27b")
response = llm.invoke(
    f"Summarize:\n{docs[0].page_content[:5000]}"
)

print(response.content)