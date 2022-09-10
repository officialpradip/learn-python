"""
Write a Python program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a person's email address, add a new name and email address, 
change an existing email address, and delete an existing name and email address. 
The program should pickle the dictionary and save it to a file when the user exits the program. 
Each time the program starts, it should retrieve the dictionary from the file and unpickle it.
"""
""""
solution boilerplate
dict={
    "name":"pradip",
    "email":"pradip@gmail.com"
}
print(dict)

#to add
dict["shyam"]="shyam@gmail.com"

print(dict)
to update
dict["shyam"]="shyam1@gmail.com"

print(dict)

to delete
del dict["shyam"]

print(dict)
"""
#from curses.ascii import isdigit
import pickle
VIEW_ALL_CONTACTS = 1
VIEW_A_CONTACTS = 2
ADD_A_CONTACTS = 3
EDIT_A_CONTACTS = 4
DELETE_A_CONTACTS = 5
Exit_Programs = 6

contacts_file = ".//contacts.dat"


def main():
    #contacts = {}
    contacts = unpickleAndRead(contacts_file)
    # contacts["Pradip"] = "pradip@gmail.com"
    # contacts["Dip"] = "dip@gmail.com"
    # contacts["Ram"] = "ram@gmail.com"

    choice = None
    while choice != Exit_Programs:
        print("Welcome to Email Contact Manager")
        print("------------------")
        print(VIEW_ALL_CONTACTS, " View Contacts", sep="")
        print(VIEW_A_CONTACTS, " View a Contacts", sep="")
        print(ADD_A_CONTACTS, " Add Contacts", sep="")
        print(EDIT_A_CONTACTS, " Update Contacts", sep="")
        print(DELETE_A_CONTACTS, " Delete Contacts", sep="")
        print(Exit_Programs, " Exit\n", sep="")

        choice = input("Enter Your choice(1-6): ")
        while not (choice.isdigit() == True and int(choice) >= 1 and int(choice) <= 6):
            print("Enter the value between 1 to 6")
            choice = input("Enter Your choice(1-6):")
        choice = int(choice)

        if choice == VIEW_ALL_CONTACTS:
            viewAllContacts(contacts)
        elif choice == VIEW_A_CONTACTS:
            viewAContacts(contacts)
        elif choice == ADD_A_CONTACTS:
            addAContacts(contacts)
        elif choice == EDIT_A_CONTACTS:
            editAContacts(contacts)
        elif choice == DELETE_A_CONTACTS:
            deleteAContacts(contacts)
        elif choice == Exit_Programs:
            exitPrograms(contacts, contacts_file)

    # viewAllContacts(contacts)
    # viewAContacts(contacts)
    # addAContacts(contacts)


# def printMenu():
#     print("Welcome to Email Contact Manager")
#     print("------------------")
#     print("1. View Contacts")
#     print("2. View a Contacts")
#     print("3. Add Contacts")
#     print("4. Update Contacts")
#     print("5. Delete Contacts")
#     print("6. Exit")

def presskeyToContinue():
    input("\nPress 'Enter'to Continue..")
    print()


def viewAllContacts(contacts):
    print("\nContacts")
    print("------------")
    if len(contacts) <= 0:
        print("No any contacts")
    else:
        for name, email in contacts.items():
            print(name, "(", email, ")", sep="")

    presskeyToContinue()


def viewAContacts(contacts):
    print("\n View Contact")
    print("---------")
    name = input("Enter the name of contact you want to view: ")
    email = ""

    for key in contacts.keys():
        if key.lower() == name.lower():
            name = key
            email = contacts[key]
    if len(email) != 0:
        print(name, "(", email, ")", sep="")
    else:
        print("Your contact name doesn't exist")

    presskeyToContinue()


def addAContacts(contacts):
    print("\n Add Contact")
    name = input("Enter the Name: ")
    email = input("Enter the email ")

    isContactExist = False
    for key in contacts.keys():
        if key.lower() == name.lower():
            print("\nContact already exist")
            isContactExist = True
            break
    #
    if isContactExist == False:
        contacts[name] = email
        print("\nContact added")

    presskeyToContinue()


def editAContacts(contacts):
    print("\nUpdate Contact")
    print("---------")
    name = input("Enter the Name: ")

    if name in contacts:
        email = input("Enter the email ")
        contacts[name] = email
        print(f"{name} is updated to {email}")
    else:
        print(f"{name} not found")

    presskeyToContinue()


def deleteAContacts(contacts):
    print("\nDelete Contact")
    print("---------")
    name = input("Enter the name of contact you want to remove: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} info deleted")
    else:
        print(f"{name} not found")

    presskeyToContinue()


def exitPrograms(contacts, contactsFile):
    pickleAndWrite(contacts, contactsFile)


def pickleAndWrite(contacts, contactsFile):
    try:
        outputFile = open(contactsFile, "wb")
        pickle.dump(contacts, outputFile)
    except Exception as ex:
        print("An error occured while writing to contacts file:", ex)
    else:
        outputFile.close()


def unpickleAndRead(contactsFile):
    contacts = {}

    try:
        inputFile = open(contactsFile, "rb")
        contacts = pickle.loads(inputFile)
    except FileNotFoundError:
        print("File Not exist")
    except EOFError:
        print("Error occured while reading")
    except Exception as ex:
        print("An error occured while reading to contacts file:", ex)
    else:
        inputFile.close()

    return contacts

    # call method
main()
