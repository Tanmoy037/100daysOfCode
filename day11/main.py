## Blackjack Project ##



import random
from art import logo



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def user_card():
    total = 0
    while total < 22:
        total_card = random.choice(cards)
        total += total_card
        return total
    
print (user_card())



# def delear_card():
#     delear_card = random.choice(cards)
#     return delear_card


