import colorama
from colorama import Fore as F, Style
from textblob import TextBlob

colorama.init()
print(f"{F.CYAN}🐍 Welcome to Sentiment Spy! 🐍{Style.RESET_ALL}")
name = input(f"{F.MAGENTA}Name: {Style.RESET_ALL}").strip() or "Mystery Agent"
h = []

while 1:
    x = input(f"{F.GREEN}>> {Style.RESET_ALL}").strip()
    if not x:
        print(f"{F.RED}Enter some text!{Style.RESET_ALL}")
        continue
    c = x.lower()

    if c == "exit":
        print(f"Bye, Agent {name}! 👋")
        break
    if c == "reset":
        h.clear()
        print("History cleared!")
        continue
    if c == "history":
        for i, (t, p, s) in enumerate(h, 1):
            print(i, t, f"Polarity: {p:.2f}", s)
        if not h:
            print("No history!")
        continue

    p = TextBlob(x).sentiment.polarity
    s = "Positive" if p > 0.25 else "Negative" if p < -0.25 else "Neutral"
    e = {"Positive": "😊", "Negative": "😞", "Neutral": "😭"}[s]
    h.append((x, p, s))
    print(f"{e} {s} sentiment! Polarity: {p:.2f}")


#activity2
import random
from colorama import Fore as F,init
init(autoreset=True)

D={"beaches":["Bali","Maldives","Phuket"],"mountains":["Alps","Rockies","Himalayas"],"cities":["Tokyo","Paris","New York"]}
J=["Too many bugs!","It had a virus!","Because of hot spots!"]

n=input("Name: ")
print(F.CYAN+f"Hi {n}! TravelBot 🌍")
print("recommend | packing | joke | help | exit")

while 1:
    x=input(f"{n}: ").lower()

    if "recommend" in x or "suggest" in x:
        p=input("beaches/mountains/cities: ").lower()
        if p in D: print("Try",random.choice(D[p]))
        else: print("Unknown type")

    elif "pack" in x:
        print("Pack clothes, charger & check weather.")

    elif "joke" in x or "funny" in x:
        print(random.choice(J))

    elif "help" in x:
        print("recommend | packing | joke | help | exit")

    elif "exit" in x or "bye" in x:
        print("Safe travels! 👋"); break

    else: print("Could you rephrase?")
