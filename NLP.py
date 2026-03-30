import requests
from config import HF_API_KEY
API_URL="https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"
headers={"Authorization":f"Bearer{HF_API_KEY}"}
Topics=["Sports","Technology","Business","Politics","Health"]

def ask_hf(text):
    r=requests.post(API_URL,headers=headers,json={"inputs":text,
                "parameters":{"candidate_labels":Topics}})
    r.raise_for_status()
    return r.json()

def show(text,preds):
    preds=sorted(preds,key=lambda x:x["score"],reverse=True)
    top=preds[0]
    print("\n News Topic Classifier ")
    print("Headline:",text)
    print(f"Best: {top['label']} ({round(top['score']*100,1)}%)")
    print("\n Top 3:")
    for i,p in enumerate(preds[:3],1):
        print(f"{i}. {p['label']} {round(p['score']*100,1)}%")
def main():
    while True:
        text = input("\n Enter headline(or 'exit'):")
        if text.lower() == "exit":
            break
        if text.strip():
            try:
                show(text, ask_hf(text))
            except Exception as e:
                print("Error:", e)

if __name__ == "__main__":
    main()