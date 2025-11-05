print("hello i am your minecraft assistat. what is your name: ")

name = input()

print(f"nice to meet you {name}")

print("how are you feeling today (good/bad) : ")
mood = input().lower()

if mood == "good":
    print("i'm happy to hear that")
elif mood == "bad":
    print("i'm sorry to hear that.")

else:
    print("i see. sometimes it is hard to put your feelings into words.")

print(f"it was nice chatting with you {name}. bye")
