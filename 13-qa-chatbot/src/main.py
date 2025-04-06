import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please provide a valid API key in the environment variables.")


genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel(model_name="gemini-2.0-flash")


@cl.on_chat_start
async def handle_chat_start():
    print("\n 🔥 Chat started")
    await cl.Message(content="Hello! How can I help you today?").send()


@cl.on_message
async def handle_message(message: cl.Message):
    prompt = message.content
    print("\n 📩 User message received:", prompt)

    response = model.generate_content(prompt)
    response_text = response.text if hasattr(response, "text") else ''

    await cl.Message(content=response_text).send()
