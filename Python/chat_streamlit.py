import streamlit as st
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

# Set up the Streamlit app
def app():
    # Set up the page title and input box for user messages
    st.set_page_config(page_title='Simple Chatbot', layout='wide')
    st.title('Simple Chatbot')
    user_input = st.text_input("You:", default_prompt)

    # Get the response from the OpenAI API and output it to the chat window
    if st.button('Send'):
        bot_response = get_response(user_input)
        st.text_area("Bot:", value=bot_response, height=200)

if __name__ == "__main__":
    app()
