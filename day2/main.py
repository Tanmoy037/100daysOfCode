# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# Example Input
# 39
# Example Output
# 3 + 9 = 12
# 12



# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
two_sum = int(two_digit_number[0]) + int(two_digit_number[1])
print(two_sum)


score = 0
height = 1.8
isWinning = True

# f-String
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")



# tip calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print ("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = bill + (bill * (tip / 100))
bill_per_person = bill_with_tip / people
rounded_bill_per_person = round(bill_per_person, 2)

print(f"Each person should pay: ${rounded_bill_per_person}")