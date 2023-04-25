import openai
import os

openai.api_key = "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"
profile1 = {
    "Name": "123",
    # ...
    "interests": ["art", "go out with friends", "videogames", "theater", "meditation"],
}

profile2 = {
    "Name": "123",
    # ...
    "interests": ["videogames", "gardening", "photography", "art", "soccer"],
}

# Find common interests
common_interests = list(set(profile1["interests"]).intersection(profile2["interests"]))

# Create a specific prompt to highlight common interests
prompt = f"Write a statement from Profile 1 to Profile 2 based on their common interests: {common_interests}."

# Call the OpenAI API to generate a response
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=100,
    n=3,
    stop=None,
    temperature=0.1,
)

# Extract the generated sentence from the response
statement = response.choices[0].text.strip()

# Print all responses from the API

list_of_responses = response.choices

for response in list_of_responses:
    print(response.text)

# print(statement)
