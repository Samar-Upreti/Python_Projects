from Calculation_Logic import maths_logics as logic
import os

#-----------------------
#     For Terminal User
#------------------------

def user_input():
    a = input("Enter :")
    return a

#Menu For Terminal Users
a = None
MENU = [
    ("Find Square", logic.sq),
    ("Find Even",    logic.is_even),
    ("Find Odd",   logic.is_odd),
    ("Find Circumference",    logic.circumference_circle),
    ("Find Are Of Spahere",    logic.area_sphere),
    ("Exit",    None),
]

def main():

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "=" * 55)
        print(" Simple Calculator ")
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

        num = int(user_input())
        print(action(num))

        input("\n  Press Enter to return to menu...")

if __name__ == "__main__":
    main()