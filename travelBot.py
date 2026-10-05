#activity2
import random, re
from colorama import Fore,init
init(autoreset=True)

D={"beaches":["Bali","Maldives","Phuket"],
   "mountains":["Alps","Rockies","Himalayas"],
   "cities":["Tokyo","Paris","New York"]}

J=["Why dont programmers like nature? Too many bugs!","Why did the computer go to the doctor? It had a virus!","Why do travelers always feel warm? Because of all their hot spots!"]

n=input("Name: ")
print(F.CYAN+f"Hi {n}! TravelBot 🌍")
print("recommend | packing | joke | help | exit")

def n(x):
    return re.sub(r"\s+", " ", x.strip().lower())

def rec():
    while 1:
        p = n(input(Fore.YELLOW + "Beaches, mountains or cities? "))
        if p not in D:
            print(Fore.RED + "Invalid choice!")
            continue
        s = random.choice(D[p])
        print(Fore.GREEN + f"How about {s}?")
        a = input(Fore.YELLOW + "Like it? (yes/no): ").lower()
        if a == "yes":
            print(Fore.GREEN + "Awesome! Enjoy {s}!")
            return

def pack():
    l = n(input(Fore.YELLOW + "Where to? "))
    d = n(input(Fore.YELLOW + "How many days? "))
    print(f"Packing tips for {l} for {d} days:\n- Versatile Clothing\n- Toiletries\n- Travel Documents\n- Check Weather")

def chat():
    name = input("Your name? ")