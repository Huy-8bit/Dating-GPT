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
    n=3,  # Generate 5 responses
    stop=None,
    temperature=0.7,  # Increase temperature for more diverse responses
)

# Extract the generated sentences from the response
list_of_responses = response.choices

# Print all responses from the API
for response in list_of_responses:
    print(response.text.strip())
    message_translate = translate.translate(response.text.strip(), "en", "vi")
    print(message_translate)
    print("------------------------")

# print(statement)



# Hey! I see that we have some common interests. Do you like to play any specific videogames? I'm really into art too. What kind of art do you like?
# Chào!Tôi thấy rằng chúng tôi có một số lợi ích chung.Bạn có thích chơi bất kỳ trò chơi video cụ thể nào không?Tôi cũng thực sự thích nghệ thuật.Bạn thích loại nghệ thuật nào?
# ------------------------
# Hey, I saw that we have a couple of common interests. I'm really into videogames and art too. It would be awesome to talk about those things with you sometime.
# Này, tôi thấy rằng chúng ta có một vài lợi ích chung.Tôi cũng thực sự thích trò chơi điện tử và nghệ thuật.Thật tuyệt vời khi nói về những điều đó với bạn.
# ------------------------
# Hey! I noticed that we have a lot of common interests, like videogames and art. That's really cool!
# Chào!Tôi nhận thấy rằng chúng tôi có rất nhiều sở thích chung, như trò chơi điện tử và nghệ thuật.Thật là tuyệt!