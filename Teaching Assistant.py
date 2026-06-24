def answer_question(question):
    question = question.lower()
    if "python" in question:
        return "Python is a programing language used to create games, apps, and websites."
    elif "planet" in question:
        return "There are 8 planets in our solar system."
    elif "water" in question:
        return "Water is important beacuse all living things need it to survive."
    elif "computer" in question:
        return "A computer is an electronic device that processes information."
    elif "math" in question:
        return "Math helps us solve problems using numbers."
    else:
        return "Thats a great question! Please ask your teacher for more details."
history = []
print("AI Teaching Assistant")
print("Type 'exit' to stop.\n")
while True:
    question = input("Ask a question: ")
    if question.lower()== "exit":
        print("\nGoodbye!")
        break
    answer = answer_question(question)
    history.append((question, answer))
    print("\n Answer:")
    print(answer)
    print("\n----- Conversation History -----")
    count = 1
    for q, a in history:
        print(f"\nQ{count}: {q}")
        print(f"A{count:} {a}")
        count += 1
        print("\n---------------------------------\n")