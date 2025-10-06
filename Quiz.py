class Quiz:
    def __init__(self):
        self.q = {"Capital of Austrlia?": "Canberra", "60 + 7 = ?": "67", "Color of sky?": "Blue"}
        self.score = 0

    def start(self):
        for ques, ans in self.q.items():
            if input(ques + " ").strip().capitalize() == ans.capitalize():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! Ans: {ans}\n")
        print(f"Your Score: {self.score}/{len(self.q)}")

Quiz().start()