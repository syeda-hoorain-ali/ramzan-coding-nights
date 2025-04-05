import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    print("\n 🔥 Chat started")
    await cl.Message(content="Hi! How can I help you?").send()

@cl.on_message
async def main(message: cl.Message):
    print("\n 📩 User message received:", message.content)
    print(cl.chat_context.to_openai())

    response = f"You said: {message.content}"
    await cl.Message(content=response).send()
