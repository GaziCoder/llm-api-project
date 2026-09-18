import os

from google import genai
import dotenv

dotenv.load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

chat = client.chats.create(
    model="gemini-3.6-flash",
    config={
        "system_instruction": "You are a helpful assistant."
    }
)

print("Agent started. Type 'exit' to stop.")

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        break

    response = chat.send_message(prompt)
    print("Agent:", response.text)