from django.shortcuts import render
import openai
import os

# Authenticate to the OpenAI API
secret_key = os.getenv("OPEN_AI_KEY")
openai.api_key = secret_key

# Define a function to get the response from ChatGPT
def get_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response["choices"][0]["text"]

def symptoms(request):
    if request.method == "POST":
        user_input = request.POST.get('symptoms')
        # Prompt for the model
        prompt = f"I have symptoms of {user_input}. Can you help me identify the possible causes?"
        response = get_response(prompt)
        return render(request, 'symptoms.html', {"response": response})
    return render(request, 'symptoms.html')