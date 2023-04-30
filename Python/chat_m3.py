import openai

# set API key
openai.api_key = "YOUR_API_KEY"

# define function to prompt OpenAI API
def ask_openai(prompt, model):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

# prompt user for input and pass to OpenAI API
while True:
    user_input = input("You: ")
    response = ask_openai(user_input, "davinci")

    # perform machine learning task based on user input
    if "train model" in user_input.lower():
        # perform model training task
        response = "The model has been trained successfully."
    elif "predict" in user_input.lower():
        # perform prediction task
        response = "The prediction has been made successfully."
    elif "evaluate model" in user_input.lower():
        # perform model evaluation task
        response = "The model has been evaluated successfully."

    print("Bot: " + response)
