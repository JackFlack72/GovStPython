import pickle
from employee import Employee

# Constants for menu choices
LOOKUP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = "employees.dat"

def main():
    employees = load_employees()

    choice = 0
    while choice != QUIT:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == LOOKUP:
                lookup_employee(employees)
            elif choice == ADD:
                add_employee(employees)
            elif choice == CHANGE:
                change_employee(employees)
            elif choice == DELETE:
                delete_employee(employees)
            elif choice == QUIT:
                save_employees(employees)
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid integer.")
        print()

def load_employees():
    try:
        input_file = open(FILENAME, "rb")
        emp_dict = pickle.load(input_file)
        input_file.close()
    except IOError:
        emp_dict = {}
    return emp_dict

def save_employees(emp_dict):
    output_file = open(FILENAME, "wb")
    pickle.dump(emp_dict, output_file)
    output_file.close()

def display_menu():
    print("Menu")
    print("-" * 65)
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Change an existing employee")
    print("4. Delete an employee")
    print("5. Quit the program")
    print()

def lookup_employee(employees):
    emp_id = input("Enter an employee ID number: ")
    if emp_id in employees:
        print(employees[emp_id])
    else:
        print("The specified ID number was not found")

def add_employee(employees):
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID number: ")
    department = input("Enter employee department: ")
    title = input("Enter employee title: ")

    if emp_id not in employees:
        emp = Employee(name, emp_id, department, title)
        employees[emp_id] = emp
        print("The new employee has been added.")
    else:
        print("An employee with that ID number already exists.")

def change_employee(employees):
    emp_id = input("Enter employee ID number: ")
    if emp_id in employees:
        name = input("Enter the new name: ")
        department = input("Enter the new department: ")
        title = input("Enter the new title: ")

        emp = employees[emp_id]
        emp.set_name(name)
        emp.set_department(department)
        emp.set_title(title)
        print("Employee information updated.")
    else:
        print("The specified ID number was not found.")

def delete_employee(employees):
    emp_id = input("Enter employee ID number: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee information deleted.")
    else:
        print("The specified ID number was not found.")

if __name__ == "__main__":
    main()