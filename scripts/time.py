import openai
import os

# Set up the OpenAI API client
#openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_key = "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"

# Define the prompt that you want the API to generate text for
prompt = "Once upon a time"

# Set the parameters for the API request
params = {
    "engine": "text-davinci-002",
    "prompt": prompt,
    "max_tokens": 100,
    "temperature": 0.5,
}

# Send the request to the API
response = openai.Completion.create(**params)

# Print the generated text
print(response.choices[0].text)