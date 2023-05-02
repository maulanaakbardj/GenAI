import openai
import requests
from io import BytesIO
from PIL import Image
import os

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION_ID")

def generate_response(prompt):
    response = openai.Completion.create(
        engine="dall-e-2",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="url",
    )
    url = response["data"][0]["url"]
    image = Image.open(BytesIO(requests.get(url).content))
    return image

def chat():
    print("Welcome to the DALL-E chatbot!")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        prompt = f"User: {user_input}\nBot:"
        response = generate_response(prompt)
        image = generate_image(response)
        image.show()

if __name__ == "__main__":
    chat()
