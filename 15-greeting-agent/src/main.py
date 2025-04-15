import pyttsx3
import asyncio
import speech_recognition as sr

from pyttsx3.voice import Voice
from agents import Runner
from openai.types.responses import ResponseTextDeltaEvent
from agent import agent, config

async def main() -> None:

    engine = pyttsx3.init()
    voices: list[Voice] = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('------ Listening ⏺ ------')
        audio = r.listen(source)

        try:
            user_question = r.recognize_google(audio)
            result = Runner.run_streamed(agent, user_question, run_config=config)
        
            async for event in result.stream_events():
                if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                    print(event.data.delta, end="", flush=True)
                    
            engine.say(result.final_output)
            engine.runAndWait()

        except LookupError:
            print("Could not understand audio")
            engine.say("Could not understand audio")
            engine.runAndWait()

        except Exception as e:
            print(e)


if __name__ == "__main__":
    asyncio.run(main())
