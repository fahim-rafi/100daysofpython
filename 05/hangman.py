from urllib.request import urlopen
import json

placeholder = []
lives = 6
game_over = False
word_url = "https://random-word-form.herokuapp.com/random/noun"
response = urlopen(word_url)
word = json.loads(response.read())[0]
print(word)

for letter in word:
    placeholder += "_"

print(f"The word is: {placeholder}")

while game_over is False:
    guess = input("Please enter a letter: ").lower()

    print(f"You've entered '{guess}'")

    for i in range(len(word)):
        letter = word[i]
        if guess == letter:
            placeholder[i] = guess
            print(f"The word is: {placeholder}.\nYou have {lives} lives left.")

    if guess not in word:
        lives -= 1
        print(f"The word is: {placeholder}.\nYou have {lives} lives left.")
        if lives == 0:
            print(f"The word was {word}.\nYou have {lives} lives left.")
            print("You lost!")
            game_over = True

    if "_" not in placeholder:
        print(f"The word was {word}.\nYou had {lives} lives left.")
        print("You win!")
        game_over = True
