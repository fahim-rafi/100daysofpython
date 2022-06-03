import random

num = random.randint(1, 100)
print(num)


def start_game():
    print("Hi! This is a simple number guessing game.\nThe number will be between 1 and 100.")
    difficulty = input(
        "Please choose between the 'easy' or 'hard' difficulty: ")
    return difficulty


difficulty = start_game()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5


end_game = False

while end_game is False:
    print(f"You have {attempts} attempts remaining.")
    guess_num = int(input("Make a guess: "))

    if guess_num == num:
        print("You have correctly guessed the number! You win!")
        end_game = True
    elif guess_num > num:
        print("Sorry! The number you've picked is too high")
        attempts -= 1
    elif guess_num < num:
        print("Sorry! The number you've picked is too low")
        attempts -= 1

    if attempts == 0:
        print("Sorry! You've run out of attempts. Best of luck next time!")
        end_game = True
