#activity2
import random, re
from colorama import Fore,init
init(autoreset=True)

D={"beaches":["Bali","Maldives","Phuket"],
   "mountains":["Alps","Rockies","Himalayas"],
   "cities":["Tokyo","Paris","New York"]}

J=["Why dont programmers like nature? Too many bugs!","Why did the computer go to the doctor? It had a virus!","Why do travelers always feel warm? Because of all their hot spots!"]

def n(x):
    return re.sub(r"\s+", " ", x.strip().lower())

def rec():
    while 1:
        print(Fore.YELLOW + "TravelBot: Beaches, mountains, or cities?")
        p = input(Fore.YELLOW + "You: ")
        p = n(p)
        if p in D:
            suggestion = random.choice(D[p])
            print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
            print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
            answer = input(Fore.YELLOW + "You: ").lower()

            if answer == "yes":
                print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
            elif answer == "no":
                print(Fore.RED + "TravelBot: Let's try another.")
                rec()
            else:
                print(Fore.RED + "TravelBot: I'll suggest again.")
                rec()
        else:
            print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
            rec()


def pack():
    l = n(input(Fore.YELLOW + "Where to? "))
    d = n(input(Fore.YELLOW + "How many days? "))
    print(f"Packing tips for {l} for {d} days:\n- Versatile Clothing\n- Toiletries\n- Travel Documents\n- Check Weather")

def joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(J)}")
    print(Fore.YELLOW + f"TravelBot: {random.choice(J)}")

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot! 🌍")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = n(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            rec()
        elif "pack" in user_input or "packing" in user_input:
            pack()
        elif "joke" in user_input or "funny" in user_input:
            joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chat()
