import random
from logo import logo

play = True
game_run = True
section = "-" *70
greet = "WELCOME TO THE GAME >>> How to win? BEAT THE COMPUTER! <<<\n".center(len(section))
game_over = "x" * 35

def number_text(guess):
    if int(guess) > pc_num:
        print("..try a smaller number") 
    elif int(guess) < pc_num:
        print("..try a higher number")

print(logo)
print(greet)

while play:
    pc_num = random.randrange(1,101)
    while True:
        print("\nChoose version easy/hard: ")
        version = input(">>> ")
        if version == "easy":
            lives = 10
            break
        elif version == "hard":
            lives = 5 
            break
        else:
            print("The specified version is not valid, please try again..\n")

    while game_run:
        if lives <1 :
            print("\n" + game_over + "\nYou have no more lives..")
            print(f"The guessing number was >>> {pc_num} <<< ")
            print("GAME OVER\n" + game_over + "\n")
            # print("\n" + game_over + "\nYou have no more lives..game over..\n" + game_over + "\n")
            break

        print(f"\nLives: {lives}")
        while True:
            guess = input("Guess the number 1-100:\n>>> ")
            if not guess.isdigit():
                print("Invalid entry, please try again..\n")
            elif int(guess) > 100:
                print("The maximum number is 100, please try again..\n")
            elif guess.isdigit():
                break
            

        if int(guess) == pc_num:
            print("\n" + game_over + "\nYou guessed the number! Amazing!\n" + game_over + "\n")
            break

        elif int(guess) != pc_num:
            number_text(guess)
            lives -= 1
        
    while True:
        again = input("New game? y/n\n>>> ")
        if again == "y":
            break
        elif again == "n":
            print("Hope to see you soon, bye.")
            quit()
        else:
            print("Invalid entry..I quit")
            quit()