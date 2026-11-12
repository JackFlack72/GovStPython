from pet import Pet

def main():
    # Prompt for pet information
    name = input("Enter the name of the pet: ")
    animal_type = input("Enter the type of animal: ")
    age = input("Enter the age of the pet: ")

    # Create Pet object
    my_pet = Pet(name, animal_type, age)

    # Display data
    print("Here is the data that you entered:")
    print(my_pet)

if __name__ == "__main__":
    main()