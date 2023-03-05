# for this module's practice:
# we will be making a password generator

# created by : C0SM0

# import random module, "r"
import random as r 

# banner
print("Password Generator")

# empty password variable
password = ""

# variables for password generation
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "~!@#$%^&*()_+<>?:{}|\][';/.,']"
all_characters = lowercase+uppercase+numbers+symbols

# user input, password length
password_length = int(input("Enter the number of characters for your password : "))

# generate password
for i in range(password_length):
    # gets random character
    character = r.choice(all_characters)
    # adds random character to password
    password += character

# output password
print(password)

# feel free to keep practicing, here are some more ideas
"""
- rock paper scissors, dice simulator, coin flipper
- learn to use other modules like 'datetime', 'math', or 'regular expressions'
"""