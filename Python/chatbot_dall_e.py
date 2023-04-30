import openai
import requests
from requests.structures import CaseInsensitiveDict

import json

QUERY_URL = "https://api.openai.com/v1/images/generations"

openai.api_key = "YOUR_API_KEY"

def generate_image(prompt):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {openai.api_key}"

    model = "image-alpha-001"
    data = """
    {
        """
    data += f'"model": "{model}",'
    data += f'"prompt": "{prompt}",'
    data += """
        "num_images":1,
        "size":"512x512",
        "response_format":"url"
    }
    """

    resp = requests.post(QUERY_URL, headers=headers, data=data)

    if resp.status_code != 200:
        raise ValueError("Failed to generate image")

    response_text = json.loads(resp.text)
    return response_text['data'][0]['url']

def chat(prompt):
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

while True:
    user_input = input("You: ")
    image_prompt = chat(user_input)
    image_url = generate_image(image_prompt)
    print("Bot: Here's an image I generated:")
    print(image_url)
