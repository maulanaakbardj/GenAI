from django.shortcuts import render
import requests
import json

# Set up the OpenAI API credentials and endpoint
openai_key = "YOUR_API_KEY"
openai_endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"

# Set up the default prompt for the chatbot to respond to
default_prompt = "Hello, how can I help you today?"

# Set up the chatbot function to retrieve a response from the OpenAI API
def get_response(prompt):
    # Set up the HTTP headers and request content with the prompt and some additional parameters
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + openai_key
    }
    data = {
        'prompt': prompt,
        'max_tokens': 50,
        'temperature': 0.5
    }

    # Send the request to the OpenAI API and retrieve the response
    response = requests.post(openai_endpoint, headers=headers, data=json.dumps(data))
    response_text = response.json()['choices'][0]['text'].strip()

    return response_text

# Define the chatbot view
def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST['user_message']
        bot_response = get_response(user_message)
        return render(request, 'chatbot.html', {'bot_response': bot_response})
    else:
        return render(request, 'chatbot.html', {'bot_response': default_prompt})
