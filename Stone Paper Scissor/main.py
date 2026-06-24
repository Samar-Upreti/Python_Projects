import random as ra

def Menu():
    while True:
        print("===== Welcome =====")
        print("Options :")
        print("Enter '1' To Start")
        print("Enter '2' For Rules/Controls")
        print("Enter '3' For Exit")

        try:
            x = int(input("Choose :"))

            if x == 1:
                Start_Game()
            elif x == 2:
                Game_Controls()
            elif x == 3:
                break
            else:
                print("Incorrect Option :/")

        except ValueError:
            print("Enter Numbers Only")

def Game_Logic(computer,user):

    match (computer, user):

        case (1, 3):
            return "computer"

        case (1, 1):
            return "draw"

        case (1, 2):
            return "user"

        case (2, 1):
            return "computer"

        case (2, 2):
            return "draw"

        case (2, 3):
            return "user"

        case (3, 1):
            return "user"

        case (3, 3):
            return "draw"

        case (3, 2):
            return "computer"
                

def Game_Controls():
    print("'1' ------ > Stone")
    print("'2' ------ > Paper")
    print("'3' ------ > Scissor")

def Start_Game():

    user_score = 0
    computer_score = 0

    for _ in range(3):

        user = int(input("Choose (1-Stone, 2-Paper, 3-Scissor): "))
        computer = ra.randint(1, 3)

        print("Computer chose:", computer)

        result = Game_Logic(computer, user)

        if result == "user":
            user_score += 1
            print("You Win")

        elif result == "computer":
            computer_score += 1
            print("You Lose")

        else:
            print("Draw")

        print(f"User: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("🏆 You Won The Game!")

    elif computer_score > user_score:
        print("💻 Computer Won The Game!")

    else:
        print("🤝 Match Draw")

Menu()