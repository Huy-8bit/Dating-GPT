import json

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
        
    
            
def get_choice(profile1, profile2):
    choices = ["123123", "huy2", "huy3"]
    common_interests = list(set(profile1["interests"]).intersection(profile2["interests"]))
    print("------")
    list_matching_labels = get_matching_labels(profile1, profile2)
    # print all content of list_matching_labels
    print_content_of_list_matching_labels(list_matching_labels, profile1, profile2)
    return choices
