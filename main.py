import requests
import html

param = {
    "amount": 10,
    "difficulty": "easy",
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php?", params=param)
response.raise_for_status()
data = response.json()
question_data = data["results"]

score = 0
question_num = 0

for question in question_data:
    question_num += 1
    que = html.unescape(question['question'])
    print("----------------------------------------------")
    print(f"{question_num}){que}")
    answer = question["correct_answer"]
    guess = input("Enter your answer(true/false): ").capitalize()
    if guess == answer:
        print("Correct!!")
        score += 1
    else:
        print("Incorrect!!")

print("---------------------------")
print(f"Your Score is: {score}/10")
