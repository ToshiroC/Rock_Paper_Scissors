0import random

def game():
    player = input('\nLet\'s play Rock, Paper, Scissors! Type "r" to choose rock, "p" for paper, and "s" for scissors. ').lower()
    #The computer randomly chooses one of the options above
    bot = random.choice(["r", "p", "s"])

    #The computer's choice is returned as either "rock", "paper", or "scissors
    def choice(rps):
        if rps == "r":
            return "rock"
        elif rps == "p":
            return "paper"
        else:
            return "scissors"

    chosen = choice(bot)

    #Displays the computer's choice
    print("\nThe computer has chosen " + chosen)

    if player == bot:
        print("\nIt's a tie!")

    #Tells the user they lost based on the conditions defined in the lose function below
    elif lose(bot, player):
        print("\nYou lose!")

    else:
        print("\nYou win!")

    #Allows the player to play the game again if they wish
    retry = input("\nDo you want to play again? (Y/N) ").lower()
    if retry == "y":
        game()

    else:
        print("\nThanks for playing!")

#Defines the conditions for the user to lose the game
def lose(computer, user):
    if (computer == "r" and user == "s") or (computer == "p" and user == "r") or (computer == "s" and user == "p"):
        return True

game()


