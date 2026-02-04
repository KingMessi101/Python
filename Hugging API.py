import cohere
from config import COHERE_API_KEY
co = cohere.Client(COHERE_API_KEY)
Topics = ["sports", "tecnolodgy", "buisness", "politics", "health"] 
def ask_cohere(headline: str)
    promt = f"""
you are a news classifier

classify this headline into only one of these catagories
{', '.join(Topics)}

Headline: "{headline}"
reply with only the catagorie name
"""
    response = co.chat(
        model="c4ai-aya-expanse-8b",
        message=prompt,
        temperature = 0
    )

    return response.text.strip()

def bar():
    return "████████░░"

def show (headline, topic):
    print("\n" + "=" *60)
    print("news topic clasifier {cohere API}")
    print("=" *60)

    print("headline:", headline)
    print("BEst Topic:", topic)
    print("confedence ~90% ["+ bar() +"]")

    print("=" *60)

    def main():
    print("Welcome! Type a news headline and I'll guess the topic.")
    print("Topics:", ", ".join(TOPICS))
    print("Type 'exit' to quit.\n")

    while True:

        headline = input("Headline: ").strip()

        if headline.lower() == "exit":
            print("Bye! 🚀")
            break

        if not headline:
            print("Please type something.\n")
            continue

        try:
            topic = ask_cohere(headline)
            show(headline, topic)

        except Exception as e:
            print("Error:", e)
if __name__ == "__main__":
    main()