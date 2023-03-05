# for this module's practice:
# we will make a quiz about animal

# created by : C0SM0

# banner
print("Animal Quiz")

# question 1, q1
print("Question 1:")
q1 = input("Whales breathe air\n1) True\n2) False\n\nAnswer : ")
# checks to see if answer is correct
if q1 == "1":
    print("Correct!\n")
# checks to see if answer is incorrect
elif q1 == "2":
    print("Incorrect!\n")
# outputs message if an invalid answer was chosen
else:
    print("Input not recognized\n")

# question 2, q2
print("Question 2:")
q2 = input("Which of the following are land animals\n1) dolphin\n2) fish\n3) tiger\n\nAnswer : ")
# checks to see if answer is correct
if q2 == "3":
    print("Correct!\n")
# checks to see if answer is incorrect
elif q2 == "1" or q2 == "2":
    print("Incorrect!\n")
# outputs message if an invalid answer was chosen
else:
    print("Input not recognized\n")

# question 3, q3
print("Question 3:")
q3 = input("Select all of the carnivors\n1) t-rex\n2) velociraptor\n3) bunny\n\nAnswer : ")
# checks to see if answer is correct
if ("1" in q3 and "2" in q3) and ("3" not in q3):
    print("Correct!\n")
# checks to see if answer is incorrect
elif "3" in q3:
    print("Incorrect!\n")
# checks to see if answer is incorrect
elif ("2" in q3) and ("1" not in q3):
    print("Incorrect!\n")
# checks to see if answer is incorrect
elif ("1" in q3) and ("2" not in q3):
    print("Incorrect!\n")
# outputs message if an invalid answer was chosen
else:
    print("Input not recognized\n")

# now this code works but is not effecient
# it is repeating the same steps over and over again
# in the next module, we will learn about loops, to shorten process's like this
# consider coming back and shrotening this code with loops

# feel free to keep practicing, here are some more ideas
"""
- password authenticator
- suggest movies to a user based on their age
"""