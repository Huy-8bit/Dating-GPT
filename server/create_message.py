import translate
import openai
import os

openai.api_key = "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"


def create_message(profile1, profile2, list_matching_labels, sender, history):
    formatted_labels = []

    for label in list_matching_labels:
        if isinstance(label, str) and label in profile1 and label in profile2:
            formatted_labels.append(f"{label}-{profile1[label]}-{profile2[label]}")

    print("Formatted list_matching_labels:")
    print(formatted_labels)
    
    prompt = f"Write a statement from Profile 1 to Profile 2 based on what they have in common: {formatted_labels}. Consider the following message history:\n\n"

    print("check history")
    print(history)
    
    
    for message in history:
        prompt += f"{message['sender']} said: {message['msg']}\n"

    print("check prompt")
    print(prompt)
    # return ["1","2","3"]
    
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
    list_of_responses = []
    for choice in response.choices:
        list_of_responses.append(choice.text.strip())
    # Print all responses from the API
    # for response in list_of_responses:
    #     print(response.text.strip())
    #     message_translate = translate.translate(response.text.strip(), "en", "vi")
    #     print(message_translate)
    #     print("------------------------")

    # Return all responses from the API
    return list_of_responses
