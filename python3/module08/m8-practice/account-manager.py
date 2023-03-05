# for this module's practice:
# we will make an account manager

# created by : C0SM0

# banner 
print("Account Manager\n")

# loop code, in case of exception
while True:
    # databases
    account_db = 'accounts.txt'
    read_db = open(account_db).readlines()

    # option menu
    print("Account Options:\n1) Create Account\n2) Sign in\n")
    option = input("Option : ")

    # user input, username
    username = input("\nEnter username : ")
    # user input, password
    password = input("Enter password : ")
    # format account
    account = f"{username}=={password}"

    # otpion 1, create account
    if option == "1":
        # user input, password confirmation
        confirm_password = input("Confirm new password : ")

        # confirm password
        if password != confirm_password and "=" not in password:
            print("Invalid password\n- passwords don't match\n- password can't contain \"=\"\n")
            continue

        # updates db with new account
        else:
            with open(account_db, "w") as db:
                db.write(f"{read_db}\n{account}")
                print("Account Created, you can now sign in\n")
            continue
    
    # option 2, sign in
    elif option == "2":
        for user_account in read_db:
            if user_account.startswith(f"{username}=="):
                if user_account.endswith(f"=={password}"):
                    print("ACCESS GRANTED!")
                    break
                else:
                    print("Password is incorrect, try again\n")
                    continue

    # exception
    else:
        print("Invalid input option, try again\n")
        continue

    break

# feel free to keep practicing, here are some more ideas
"""
- add options for deleting profiles and resetting passwords in the code above
- search for certain items in a a file
"""