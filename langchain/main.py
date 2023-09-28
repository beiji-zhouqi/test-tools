from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import os


os.environ["OPENAI_API_KEY"] = "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"

llm = OpenAI()
chat_model = ChatOpenAI()


req = llm.predict("hi!")
print(req)