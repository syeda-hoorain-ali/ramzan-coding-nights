import os
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please provide a valid API key in the environment variables.")


provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)

config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

instructions1 = "You are a Greeting Agent, Your task is to greet the user with a friendly message, when someone says hi you've reply back with salam from Hoorain ali, if someone says bye then say Allah hafiz from Hoorain ali, when someone asks other than greeting then say Hoorain is here just for greeting, I can't answer anything else, sorry."

# instructions2 = "You are a greeting agent, You're speaking to a human, so be polite and concise."

agent = Agent(
    name="Greeting Agent",
    instructions=instructions1,
    model=model,
)
