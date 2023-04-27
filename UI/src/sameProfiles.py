import json
import random

# Đọc file json vào biến data
with open('C:\Dating-GPT/format_data_set.json') as f:
    data = json.load(f)

# Lấy danh sách các nhãn trong file JSON
labels1 = list(data["profile1"].keys())
labels2 = list(data["profile2"].keys())
found_index = []
found_interests = []
for i in range(15):
  # Tạo ngẫu nhiên chỉ số của hai nhãn trong labels
  index = random.randint(0, len(labels1)-1)

  # Kiểm tra xem hai nhãn có giống nhau hay không
  if index not in found_index and index == len(labels1)-1:
      interests1 = data['profile1']['interests']
      interests2 = data['profile2']['interests']

      # Tìm và in ra các sở thích giống nhau
      common_interests = set(interests1) & set(interests2)
      print("sở thích giống nhau:")
      for interest in common_interests:
          if interest not in found_interests:
            print(interest)
            found_interests.append(interest)
  elif index not in found_index and labels1[index] == labels2[index]:
      print(f"2 label hợp nhau: {labels1[index]}") 
  found_index.append(index)