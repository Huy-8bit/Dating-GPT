import translate
import openai
import os

# openai.api_key = "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"


def create_message(profile1, profile2, list_matching_labels, sender, history):
    formatted_labels = []

    for label in list_matching_labels:
        if isinstance(label, str) and label in profile1 and label in profile2:
            formatted_labels.append(f"{label}-{profile1[label]}-{profile2[label]}")


    sender_receive = ''
    if sender == 'P2':
        sender_receive = 'P1'
    else:
        sender_receive = 'P2'
         
    # prompt = f"Write a statement from {sender} to {sender_receive} based on what they have in common: {formatted_labels}.Consider the following message history:\n\n"
    
    prompt = f"Write a chat from {sender} to {sender_receive} based on what they have in common: {formatted_labels}. Consider the following message history:\n\n "
    
    print(sender + " to "+ sender_receive)
    
    for message in history:
        prompt += f"{message['sender']} said: {message['msg']}\n"


    # 'name-huy-huy','job-dev-dev',......
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
    

    # Return all responses from the API
    return list_of_responses
