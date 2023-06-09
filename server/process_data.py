import json
import create_message



def remove_said(string):
    string = string.replace("P2 said:", "")
    string = string.replace("P1 said:", "")
    return string

def replace_names(string,profile1, profile2):
    string = string.replace("P1", profile1['Name'])
    string = string.replace("P2", profile2['Name'])
    return string


def get_matching_labels(profile1, profile2):
    matching_tags = []
    for tag1 in profile1:
        if tag1 in profile2:
            if isinstance(profile1[tag1], list) and isinstance(profile2[tag1], list):
                common_items = list(set(profile1[tag1]).intersection(profile2[tag1]))
                if common_items:
                    matching_tags.append({tag1: common_items})
            else:
                if profile1[tag1] == profile2[tag1]:
                    matching_tags.append(tag1)
    return matching_tags

def print_content_of_list_matching_labels(list_matching_labels, profile1, profile2):
    for i in list_matching_labels:
        if isinstance(i, dict):
            for key, value in i.items():
                print("common", key, ":", value)
        else:
            print("common", i, ":", profile1[i])
        
    
            
def get_choice(profile1, profile2, sender, history):

    common_interests = list(set(profile1["interests"]).intersection(profile2["interests"]))
    print("------")
    list_matching_labels = get_matching_labels(profile1, profile2)
    # print all content of list_matching_labels
    # print_content_of_list_matching_labels(list_matching_labels, profile1, profile2)
    choices = create_message.create_message(profile1, profile2, list_matching_labels, sender, history)
    # choices = ["Hi", "Hello", "How are you?"]
    sender_receive = ''
    if sender == 'P2':
        sender_receive = 'P1'
    else:
        sender_receive = 'P2'
        
    result = [];
    
    for choice in choices:
        result.append(replace_names(remove_said(choice), profile1, profile2))    
    
    sender = sender_receive
    return result



