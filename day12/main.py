import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = input("Choose a difficulty. Type 'easy' or 'hard': ")

if number == "easy":
  lives = 10
  print(f"You have {lives} attempts remaining to guess the number.")
elif number =="hard":
  lives = 5
  print(f"You have {lives} attempts remaining to guess the number.")



game_number = random.randint(1,100)

def game():
    global lives
    global number
    global game_number
    while lives > 0 :
        guess = int(input("Make a guess: "))
        if guess == game_number:
            print("You got it!")
            break
        elif guess > game_number:
            print("Too high.")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number.")
        elif guess < game_number:
            print("Too low.")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number.")

    if lives == 0:
        print("You've run out of guesses, you lose.")
        

game()
print(f"The original number was {game_number}.")

    
