# contact module for 'main.py'

# creates a class for contacts
class Contact:

    # initialize instance variables
    def __init__(self, name, email, phone, database):
        self.name = name
        self.email = email
        self.phone = phone
        self.db = database

    # updates current database
    def updateDbLines(self):
        # reads current version of database
        read_db = open(self.db, "r").readlines()
        return read_db

    # updates current database
    def updateDatabase(self):
        # reads current version of database
        read_db = open(self.db, "r").read()
        return read_db

    # output profile
    def generateProfile(self):
        profile = f"\n=====\nName : {self.name}\nEmail : {self.email}\nPhone : {self.phone}\n====="
        return profile

    # write profile to file
    def writeProfile(self, profile):
        read_db = self.updateDatabase()
        # writes profile to database
        with open(self.db, "w") as contact_db:
            contact_db.write(f"{read_db}\n{profile}")

    # remove profile from file
    def removeProfile(self, profile):
        updated_db = ""
        read_db = self.updateDbLines()
        # iterates through database of contacts
        for contact in read_db:
            # checks if the contact exists
            if contact in profile:
                continue
            # writes all existing contact info that isn't part of the contact
            else:
                updated_db += contact
        # write updated database
        with open(self.db, "w") as db:
            db.write(updated_db)

    # output contact
    def outputProfiles(self):
        read_db = self.updateDatabase()
        return read_db

# main code
def main():
    print("Please run 'main.py'")

# checks running type
if __name__ == "__main__":
    main()