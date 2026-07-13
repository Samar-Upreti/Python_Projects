import random 
import os


def find_num():
    '''system take a random number based on the complexity you choose '''

    a = random.randint(10,99)
    while True:

        try:
            user_input = int(input("Guess :"))
            if a == user_input:
                print(f"You Found That :{user_input}")
                return False
            else:
                if user_input > a:
                    print("Try Lesser Value")
                elif user_input < a:
                    print("Try Greater Value")
        except ValueError:
            print("Only Integers Allowed")


def game_rule():
    '''Rules No One Care About :) (despite me)'''

    print("="*50)
    print("\t:: Computer Will Take a Random Number \n")
    print("\t:: It Will Give You Hints too..\n")
    print("\t:: Bahi Rocket Science Nahi Haiii :/ ")
    print("="*50)


MENU = [
    ("Start The Game",    find_num),
    ("Rules",     game_rule),
    ("Exit",    None)
]

def main():
    '''lovely clean terminal isn't it ?'''

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "=" * 55)
        print("  Number Guessing (99% Failed)")
        print("=" * 55)
        for i, (label, _) in enumerate(MENU, 1):
            print(f"   {i}.  {label}")
        print("=" * 55)

        try:
            choice = int(input("\n  Enter option: ").strip())
        except (ValueError, KeyboardInterrupt):
            print("\n  Invalid input. Try again.")
            input("\n  Press Enter to continue...")
            continue

        if choice < 1 or choice > len(MENU):
            print("  Out of range.")
            input("\n  Press Enter to continue...")
            continue

        label, action = MENU[choice - 1]
        if action is None:
            print("\n  Goodbye!\n")
            break

        action()

        input("\n  Press Enter to return to menu...")

if __name__ == "__main__":
    main()
