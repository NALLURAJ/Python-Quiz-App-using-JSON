import random
import json
#LOAD JSON
def load_ques():
    with open("questions.json", "r") as f:
        questions=json.load(f)["questions"]
    return questions

#RANDOM QUESTIONS
def random_ques(questions,num_ques):
    if num_ques > len(questions):
        num_ques = len(questions)
    random_questions = random.sample(questions,num_ques)
    return random_questions

#ASK QUESTIONS
def ask_questions(questions):
    print(questions["question"])
    for i, option in enumerate(questions["options"]):
        print(f' {i+1}. {option}')
    number = int(input("Select the correct answer: "))
    if number < 1 or number >len(questions["options"]):
        print("Invalid Choice")
        return False
    correct = questions["options"][number - 1] == questions["answer"]
    return correct

#MAIN CONTENT !
ques = load_ques()
total_questions = int(input("Enter Number of Questions: "))
random_question = random_ques(ques, total_questions)
correct = 0
for question in random_question:
    is_correct = ask_questions(question)
    if is_correct:
        correct += 1
        print("---------------------------")
print("Summary")
print(f"Total Questions: {total_questions} and Your score: {correct}")