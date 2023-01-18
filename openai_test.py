import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response():
    question = input("Ask your question here: ")
    print(f"Is this what you said? {question}")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.text

get_response()
