import requests
import random
import html
education_category_id=9
api_url=f"https://opentdb.com/api.php?amount=10&category=&type=multiple"
def get_education_questions():
    response=requests.get(api_url)
    if response.status_code==200:
        data=response.json()
        if data['response_code']==0 and data['results']:
            return data['results']
    return None
def run_quiz():
    questions=get_education_questions()
    if not questions:
        print("Failed to fetch educational questions")
        return
    score=0
    print("Welcome to education Quiz\n")
    for i,q in enumerate(questions,1):
        question=html.unescape(q['question'])
        correct=html.unescape(q['correct_answer'])
        incorrects=[html.unescape(a) for a in q['incorrect_answers']]
        options=incorrects+[correct]
        random.shuffle(options)
        print(f"Question{i}: {question}")
        for idx,option in enumerate(options,1):
            print(f"{idx}.{option}")
        while True:
            try:
                choice=int(input("\n Your answer(1-4):"))
                if 1<=choice<=4:
                    break
            except ValueError:
                pass
            print("Invalid input! please enter 1-4")
        if options[choice-1]==correct:
            print("correct\n")
            score+=1
        else:
            print(f"Wrong! correct answer:{correct}\n")
    print(f"Final score:{score}/{len(questions)}")
    print(f"Percentage:{score/len(questions)*100:.1f}%")
if __name__=="__main__":
    run_quiz()