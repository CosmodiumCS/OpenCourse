# for this module's practice:
# we will be building a contact page [phonebook]

# import contact script, "c"
from Contact import Contact as c

def add_contact(info, profile):
    info.writeProfile(profile)
    return f"The profile:{profile}\nWas added"

def remove_contact(info, profile):
    info.removeProfile(profile)
    return f"The profile:{profile}\nWas removed"

def edit_contact(option, db):
    # user input, name, email, phone
    if option == "1" or option == "2":
        name = input("Enter Contact's Name : ")
        email = input("Enter Contact's Email : ")
        phone = input("Enter Contact's Phone Number : ")

        # class object
        contact_information = c(name, email, phone, db)
        # generates phone profile for editing database
        phone_contact = contact_information.generateProfile()
 
    # option 1, adds contact
    if option == "1":
        print(add_contact(contact_information, phone_contact))
        return True
    # option 2, removes contact
    elif option == "2":
        print(remove_contact(contact_information, phone_contact))
        return True
    # option 3, outputs contacts
    elif option == "3":
        read_db = open(db).read()
        print(read_db)
        return True
    # exception
    else:
        print("Invalid argument added")
        return False

# main code
def main():
    # loops code, in case of exception
    while True:
        # databse
        database = "contacts.txt"

        # banner
        print("Phone Book")

        # options menu
        print("Choose an option:\n1) Add Contact\n2) Remove Contact\n3) Display Contacts\n")
        # user input, option
        option = input("Option : ")
        # handles contact info, depending on option
        process = edit_contact(option, database)
        
        # detects if process was sucessful
        if process == True:
            break
        else:
            continue

# checks running type
if __name__ == "__main__":
    main()

# feel free to keep practicing, here are some more ideas
"""
- allow users to store addresses
- optimize previous projects with your new found knowledge
"""