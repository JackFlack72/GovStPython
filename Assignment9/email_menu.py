import os
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Always read/write email.dat next to this script, regardless of the
# folder the program is run from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, 'email.dat')


def main():
    """Load the emails, run the menu loop, and save after each change."""
    emails = loadEmails()
    
    choice = 0
    while choice != QUIT:
        choice = getUserChoice()
        
        if choice == LOOK_UP:
            lookUp(emails)
        elif choice == ADD:
            add(emails)
            saveEmails(emails)
        elif choice == CHANGE:
            change(emails)
            saveEmails(emails)
        elif choice == DELETE:
            delete(emails)
            saveEmails(emails)
        elif choice == QUIT:
            print("Exiting program.")


def loadEmails():
    """Load and return the saved emails dictionary (or an empty one)."""
    try:
        infile = open(FILENAME, 'rb')
        emails = pickle.load(infile)
        infile.close()
    except (FileNotFoundError, EOFError):
        emails = {}
    return emails


def getUserChoice():
    """Display the menu and return a validated choice."""
    print("\nMenu")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit the program")
    
    choice = int(input("Enter your choice: "))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Valid choices are 1-5. Enter your choice: "))
    return choice


def lookUp(emails):
    """Print the email address for a name the user enters, if found."""
    name = input("Enter a name: ")
    
    if name in emails:
        print(f"Name: {name}")
        print(f"Email: {emails[name]}.")
    else:
        print("The specified name was not found.")


def add(emails):
    """Add a new name/address pair if the name isn't already present."""
    name = input("Enter name: ")
    
    if name not in emails:
        address = input("email address: ")
        emails[name] = address
        print("Name and address have been added.")
    else:
        print("That name already exists.")


def change(emails):
    """Update the address for an existing name."""
    name = input("Enter name: ")
    
    if name in emails:
        address = input("Enter the new address: ")
        emails[name] = address
        print("Information updated.")
    else:
        print("The specified name was not found.")


def delete(emails):
    """Remove a name/address pair."""
    name = input("Enter name: ")
    
    if name in emails:
        del emails[name]
        print("Information deleted.")
    else:
        print("The specified name was not found.")


def saveEmails(emails):
    """Pickle the emails dictionary to FILENAME."""
    outfile = open(FILENAME, 'wb')
    pickle.dump(emails, outfile)
    outfile.close()


if __name__ == '__main__':
    main()