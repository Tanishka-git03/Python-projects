Questions = [
    {
        "Question": "What is the capital city of Australia?",
        "Options": ["a) Sydney", "b) Melbourne", "c) Canberra", "d) Brisbane"],
        "Answer": "c"
    },
    {
        "Question": "Which planet is known as the Red Planet?",
        "Options": ["a) Jupiter", "b) Mars", "c) Venus", "d) Saturn"],
        "Answer": "b"
    },
    {
        "Question": "Who painted the Mona Lisa?",
        "Options": ["a) Vincent van Gogh", "b) Leonardo da Vinci", "c) Pablo Picasso", "d) Michelangelo"],
        "Answer": "b"
    },
    {
        "Question": "What is the chemical symbol for water?",
        "Options": ["a) H2O", "b) CO2", "c) O2", "d) N2"],
        "Answer": "a"
    },
    {
        "Question": "Which country is home to the Great Wall of China?",
        "Options": ["a) Japan", "b) India", "c) China", "d) Korea"],
        "Answer": "c"
    },
]

def run_quiz(Questions):
    score = 0
    for Question in Questions:
        print("\n" + Question["Question"])
        for option in Question["Options"]:
            print(option)
        answer = input("Enter your answer (a, b, c, d): ").lower()
        if answer == Question["Answer"]:
            print("Correct, Hurrayyy!!!\n")
            score += 1
        else:
            print("Oops! The correct answer was", Question["Answer"] + "\n")
    print(f"You got {score} out of {len(Questions)} questions correct.")

run_quiz(Questions)