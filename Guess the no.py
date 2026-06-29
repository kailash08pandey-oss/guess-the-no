import random

print("Welcome to Guess the Number Game\n")
# function for difficulty leve;l
def level():
    difficulty = input("Choose the difficulty level (Easy / Hard) ").lower()

    if difficulty == "easy":
#another function for game 
        def game():
            number = random.randint(1, 50)

            print("I am taking a number between (1-50) and you have to guess it.")

            user_guess = int(input("Guess the No.: "))
            #function for user guess 
            def check(user_guess):
                while number != user_guess:
                    if user_guess > number:
                        print("Too High")
                        user_guess = int(input("Guess again.: "))

                    elif user_guess < number:
                        print("Too Low")
                        user_guess = int(input("Guess again.: "))

                print(" Congratulations! You have guessed the number.")

            check(user_guess)

            play = input("Do you want to play the game again? (yes/no): ")

            if play.lower() == "yes":
                game()
            else:
                print("Thank you for playing.")

        game()

    elif difficulty == "hard":

        def game():
            number = random.randint(1, 100)

            print("I am taking a number between (1--100) and you have to guess it.")

            user_guess = int(input("Guess the No.: ")) 
            # function  check user guess 
            def check(user_guess):
                while number != user_guess:
                    if user_guess > number:
                        print("Too High")
                        user_guess = int(input("Guess again.: "))

                    elif user_guess < number:
                        print("Too Low")
                        user_guess = int(input("Guess again.: "))

                print("Congratulations! You have guessed the number.")

            check(user_guess)

            play = input("Do you want to play the game again? (yes/no): ")

            if play.lower() == "yes":
                game()
            else:
                print("Thank you for playing.")

        game()

    else:
        print("Invalid Difficulty!")

level()
# ok tested 
