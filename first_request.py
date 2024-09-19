import os

from openai import OpenAI
from dotenv import load_dotenv

# read the .env
load_dotenv()
CLIENT = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

my_instructions = """
You are a duck. You will answer the question in a helpful manner but do not forget to quack every few words.

My question is: What is the fastest animal on Earth?
"""
# make a call to chatGpt
print("Asking ChatGPT...")
chat_response = CLIENT.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": my_instructions}
    ]
)

# chatGpt response
chat_talk = chat_response.choices[0].message.content

print(f"ChatGpt says: {chat_talk}")