import random

# word_list = ["ardvark","baboon","camel"]

# word = random.choice(word_list)

# guess = input("Guess a letter: ").lower()

# for latter in word:
#     if latter == guess:
#         print ("Right")
#     else:
#         print ("Wrong")




word_list = ["ardvark","baboon","camel"]

word = random.choice(word_list)

print(f"The random word is: ${word}")

display = []
for latter in word:
    display.append("_")
print(display)

count = 0
while count < len(word):
    guess = input("Guess a letter: ").lower()
    for position in range(len(word)):
        latter = word[position]
        if latter == guess:
            display[position] = latter
            count += 1
    print(display)
print("You win!")

 

