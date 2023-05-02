import openai
import re
import string
import random
import os

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

def remove_articles(text):
    return re.sub(r"\b(a|an|the)\b", " ", text)

def remove_extra_whitespace(text):
    return re.sub(r"\s+", " ", text).strip()

def preprocess_text(text):
    text = remove_punctuation(text)
    text = remove_articles(text)
    text = remove_extra_whitespace(text)
    return text.lower()

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

def chat():
    print("Welcome to the chatbot!")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        prompt = f"User: {user_input}\nBot:"
        response = generate_response(prompt)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat()
