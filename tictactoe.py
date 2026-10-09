import random

def show(b):
    print(f"\n{b[0]} | {b[1]} | {b[2]}")
    print("---------")
    print(f"{b[3]} | {b[4]} | {b[5]}")
    print("---------")
    print(f"{b[6]} | {b[7]} | {b[8]}")

def win(b, s):
    return any(
        all(b[i] == s for i in x)
        for x in [
            (0, 1, 2), 
            (3, 4, 5), 
            (6, 7, 8),
            (0, 3, 6), 
            (1, 4, 7), 
            (2, 5, 8),
            (0, 4, 8), 
            (2, 4, 6)
        ]
    )

def game():
    name = input("Enter your name: ")

    while True:
        b = list("123456789")
        p = input("Choose X or O: ").upper()
        while p not in "XO":
            m = input("Invalid choice. Please choose X or O: ").upper()

        ai = "O" if p == "X" else "X"

        while True:
            show(b)

            m = int(input(f"{name}, enter your move (1-9): ")) - 1
            while m not in range(9) or b[m] in "XO":
                m = int(input("Invalid! Enter position: ")) - 1
            b[m] = p

            if win(b, p):
                show(b)
                print(f"Congrats {name} you win!")
                break
            