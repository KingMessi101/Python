
def get_words(sentence):
     return sentence.lower().split()

def similarity_score(s1,s2):
     words1=set(get_words(s1))
     words2=set(get_words(s2))
     common=words1.intersection(words2)
     score=len(common)/max(len(words1),len(words2))
     return score,common

def show_result(score):
    percent=round(score*100)
    if score>0.6:
        print("These sentences are similar")
    elif score>0.3:
        print("These are a little similar.")
    else:
        print("These are different.")
    print(f"Similarity:{percent}%")
    
print("Sentence similarity Game")
print("Type 'exit' to stop\n")

while True:
    s1=input("Enter Sentence1: ")
    if s1.lower()=="exit":
        break
    s2=input("Enter sentence2: ")
    if s2.lower()=="exit":
        break
    score,common=similarity_score(s1,s2)
    print("\n common words: ",", ".join(common) if common else "None")