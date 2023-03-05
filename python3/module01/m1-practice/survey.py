# for this module's practice:
# we will create a program that will ask a user questions
# and output the information they entered

# created by : C0SM0

# banner
print("Survey:")

# user input, first name
first_name = input("What is your first name? : ")
# user inpur, last name
last_name = input("What is your last name? : ")
# user input, age
age = input("How old are you? : ")
# user input, favorite color
favorite_color = input("What is your favorite color? : ")

# full name
full_name = first_name +" "+ last_name

# results
print(f"Here are your results, {first_name}:")
print(f"- Your name is \"{full_name}\"")
print(f"- You are {age} years old")
print(f"- Your favorite color is {favorite_color}")

# feel free to keep practicing, here are some more ideas
"""
- minimal account creator
- add/subtract/multiply/divide user inputted values together 
"""