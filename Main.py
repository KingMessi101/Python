from groq import generate_response
def run_activity():
    print("ZERO-SHOT, ONE-SHOT, FEW-SHOT LEARNING ACTIVITY")
    category = input("Enter a category (e.g., animal, food, city): ").strip()
    item = input(f"Enter a secific {category} to classify:").strip()
    if not category or not item:
        print("please fill in both fields to run the activity.")
        return
    zero_shot = f"Is {item} a {category}?Answer Yes or No."
    print("\n--- ZERO-SHOT LEARNING ---")
    print(f"Responce: {generate_response(zero_shot, temperature = 0.3, max_tokens=1024)}")
    one_shot = f"""Example:
Category: Fruit
Item: apple
Answer: Yes, apple is a fruit.
Now you try:
Category: {category}
Item: {item}
Answer:"""
    print("\n--- ONE-SHOT LEARNING ---")
    print(f"Response: {generate_response(one_shot, temperature = 0.3, max_tokens=1024)}")
    few_shot = f"""Example 1:
Category: Fruit
Item: apple
Answer: Yes, apple is a fruit.
Now you try:
Category: {category}
Item: {item}
Answer:"""
    print("\n--- FEW-SHOT LEARNING ---")
    print(f"Response: {generate_response(few_shot, temperature = 0.3, max_tokens=1024)}")
    creative_prompt = f"""Write a one sentance story about a given word.
Example 1: Word: moon
Story: The moon winked at the lovers as they shared their first kiss.
Word: {item}
Story:"""
    print("\n--- CRETAIVE FEW-SHOT EXAMPLE ---")
    print(f"Response: {generate_response(creative_prompt, temperature=0.3, max_tokens=1024)}")
print("\n--- REFLECTION QUESTIONS ---")
print("1. How did the responcesdiffer between zero-shot, one-shot and few-shot?")
print("2. Which approch gave the most helpful response?")
print("3. How did the examples influence the model's output")

if __name__ == "__main__":
    run_activity()