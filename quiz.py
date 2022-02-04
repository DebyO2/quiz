import requests
import random
import json

difficulty = input("Difficulty[easy,medium,hard]? : ")
print("\n")
url = f"https://opentdb.com/api.php?amount=1&category=18&difficulty={difficulty}&type=multiple"

# url = input("Enter url: ")

question = requests.get(url)
# question = parser.unescape(question)
data = question.content
data = data.decode('utf-8')
data = json.loads(data)['results'][0]

# print(data)
question = data["question"]
correct = data["correct_answer"]
options = list(data["incorrect_answers"])
options.append(correct)
random.shuffle(options)
# print(options)
# print(correct)

print(question)
print("\n")
j = 0
answer = options.index(correct) + 1
for i in options:
    j += 1
    print(f"({j})",i,"\n")

user_answer = int(input("answer?[1,2,3,4] : "))

if user_answer == answer:

    print("Correct, congratulations")

else:

    print(f"Nah, it's not your day today, the correct answer is {correct}")

# print(question.content)