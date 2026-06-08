def bias_mitigation_activity():
    print("\n === BIAS MITIGATION ACTIVITY ===\n")
    prompt = input("Enter a prompt:")
    print("\nAI Response:")
    if "ideal doctor" in prompt.lower():
        print("The ideal doctor is a man who is experienced and knowledgable.")
    else:
        print("A doctor should be caring, skilled, and helpful.")
    modified = input(
        "\n Modify the prompt to make it more neutral: "
    )
    print("\nNeutral AI Response: ")
    print("A doctor can be of any gender and should be caring, skilled, and helpful")
def token_limit_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")
    long_prompt = input("Enter a long paragraph: ")
    print("\nREsponse with Limited Tokens:")
    print(long_prompt[:100] + "...")
    short_prompt = input(
        "\nNow write a shorter version of the paragraph:")
    print("\n Response to short Prompt:")
    print(short_prompt)
def run_activity():
    print("\n=== AI Learning Activity===")
    print("1. Bias Mitigation")
    print("2. Token Limits")
    choice = input("Choose an Option: ")
    if choice == "1":
        bias_mitigation_activity()
    elif choice =="2":
        token_limit_activity()
    else:
        print("Invalid choice")
run_activity()