import translate
import openai
import os

openai.api_key = "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"


def create_message(profile1, profile2, list_matching_labels, sender, history):
    print("check list_matching_labels")
    print(list_matching_labels)
    labels_content = []
    for i in list_matching_labels:
        if isinstance(i, dict):
            for key, value in i.items():
                labels_content.append(value)
        else:
            labels_content.append(profile1[i])
        
    # Find common interests
    # common_interests = list(set(profile1["interests"]).intersection(profile2["interests"]))
    common_interests = labels_content
    # Create a specific prompt to highlight common interests and provided attributes
    prompt = f"Write a {', '.join(labels_content)} statement from Profile 1 to Profile 2 based on their common interests: {common_interests}. Consider the following message history:\n\n"

    for message in history:
        prompt += f"{message['sender']} said: {message['msg']}\n"

    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=3,  # Generate 3 responses
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

    # Return all responses from the API
    return list_of_responses
