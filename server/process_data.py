import translate


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
    n=5,  # Generate 5 responses
    stop=None,
    temperature=0.7,  # Increase temperature for more diverse responses
)

# Extract the generated sentences from the response
list_of_responses = response.choices

# Print all responses from the API
for response in list_of_responses:
    print(response.text.strip())

    # print(translate.translate(response.text, "en", "vi"))


# print(statement)


# Currently 3 results have 2 of the same. What should I do to make it different from all 3
