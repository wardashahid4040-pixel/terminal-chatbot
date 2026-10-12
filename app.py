import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

config = types.GenerateContentConfig(
    system_instruction="You are a sarcastic yet insightful AI mentor. Keep replies sharp and concise.",
)

chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=config,
)

print("--- AI Chatbot Initialized (Type 'exit' to quit) ---\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    print("AI: ", end="", flush=True)
    try:
        response_stream = chat.send_message_stream(user_input)
        for chunk in response_stream:
            print(chunk.text, end="", flush=True)
        print("\n")
    except Exception as e:
        print(f"\nError: {e}\n")