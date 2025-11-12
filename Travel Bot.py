import re, random
from colorama import Fore, init; init(autoreset=True)

dest={"beaches":["bali", "maldives", "phuket"],
      "mountains":["swiss alps", "rocky mountains", "himalayas"],
      "cities":["tokyo","paris","new york"]}

n=lambda t:re.sub(r"\s+"," ",t.strip().lower())

def rec():
    p=input(f"{Fore.CYAN}beaches/mountains/cities?\n{Fore.YELLOW}you: ")
    if p not in dest:return print(Fore.RED+"no such option")
    while True:
        s=random.choice(dest[p]);print(Fore.GREEN+"how about "+s+"?")
        a=input(f"{Fore.YELLOW}you (yes/no): ").lower()
        if a=="yes":return print(Fore.GREEN+"enjoy "+s+"!")
        if a=="no":return
def pack():

 l = n(input(f"{Fore.CYAN}Where?\n{Fore.YELLOW}You: "))
 d = input(f"{Fore.CYAN}Days?\n{Fore.YELLOW}You: ")

 print(f"{Fore.GREEN}Packing tips for {d} days in {l}:\n- Clothes\n- Chargers\n- Weather check")
def help():
    print(f"""{Fore.MAGENTA}

I can:

{Fore.GREEN}- recommend (or type beaches/mountains/cities)

- pack

- help

- exit""")
def chat():
    print(Fore.CYAN+"Hello! I'm TravelBot.")
    name=input(f"{Fore.YELLOW}Your name: ");print(Fore.GREEN+"Nice to meet you,",name);help()
    cmd={"recommend":rec,"suggest":rec,"pack":pack,"help":help}
    while True:
        u=input(f"{Fore.YELLOW+name}: ")
        if any(x in u for x in ["exit","bye"]):
         print(Fore.CYAN+"Safe travels, goodbye!")
         return
        matched=False
        for k,f in cmd.items():
            if k in u: f(); 
            matched=True 
            break
        else: print(Fore.RED+"Could you rephrase?")

if __name__=="__main__":
    chat()