from question import question
question_prompt = [
    "1. What sound does a dog make?\n"
    "a. Mew\nb. Bark\nc. Horn\n",

    "2. Who is the father of science?\n"
    "a. Sir Isaac Newton\nb. Charles Babbage\nc. Parrot\n"
]

questions = [
    question(question_prompt[0], "b"),
    question(question_prompt[1], "a")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print(f"You got {score}/{len(questions)} correct")


run_test(questions)
