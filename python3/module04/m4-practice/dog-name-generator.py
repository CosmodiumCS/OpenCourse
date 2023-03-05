# for this module's practice:
# we will make a dog name generator

# created by : C0SM0

# banner
print("Dog Name Generator:")

# dog name lists, gender respective
male_names = ["Duke", "Sam", "Flipper", "Elliot", "Junior"]
female_names = ["Lucy", "Bailey", "Cleo", "Sadie", "Zoe"]

# output format
output_format = "You should name your dog: "

# loop code, in case of exception
while True:
    # user inpur, gender
    print("What is your dog's gender?\n1) Male\n2) Female\n")
    dog_gender = int(input("Answer : "))

    # user input, random number
    random_number = int(input("Pick a number between 1 and 5 : "))

    # check if random number is between 1 and 5
    if random_number <= 5 and random_number >= 1:
        # checks if dog is male
        if dog_gender == 1:
            print(output_format+male_names[int(random_number)])
            break

        # checks if dog is female
        elif dog_gender == 2:
            print(output_format+female_names[int(random_number)])
            break

        # exception, gender
        else:
            print("You did not choose '1' for 'Male' or '2' for 'Female\n")
            continue

    # exception, random number
    else:
        print("Number not between 1 and 5, try again\n")
        continue

# feel free to keep practicing, here are some more ideas
"""
- vending machine
- filter specific numbers in a list [even numbers, odd numbers, prime numbers, etc]
"""