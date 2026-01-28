import requests, random

url = "https://opentdb.com/api.php?amount=5&type=multiple"
data = requests.get(url).json()

score = 0

for i, q in enumerate(data["results"], 1):
    print(f"\nQ{i}: {q['question']}")

    options = q ['incorrect_answers'] + [q['correct_answer']]
    random.shuffle(options)

    for n, opt in enumerate (options, 1):
        print(f"{n}. {opt}")

    ans = int(input("Your answer(1-4): "))
    if options[ans-1] == q["correct_answer"]:
        print("correct!")
        score =+ 1

    else:
        print(f"Wrong, Correct answer: {q['correct_answer']}")

print(f"Final score: {score}/{len(data['results'])}")
