# for this module's practice:
# we will make a program that will generate multiplication tables

# created by : C0SM0

# variables
range_limit = range(1, 13)

# iterate through each table
for table_number in range_limit:

    # banner
    print(f"\nMultiplication Table for {table_number}:")

    # iterate through each multiple
    for multiple in range_limit:
        answer = table_number * multiple
        print(f"{table_number} x {multiple} = {answer}")

# feel free to keep practicing, here are some more ideas
"""
- multiplication table with user input
    - users can ask for certain tables or to list the first 12
- a quiz that can end if a question is answered wrong
"""
