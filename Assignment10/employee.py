class Employee:
    def __init__(self, name, emp_id, department, title):
        self.__name = name
        self.__emp_id = emp_id
        self.__department = department
        self.__title = title

    # Getters
    def get_name(self):
        return self.__name

    def get_emp_id(self):
        return self.__emp_id

    def get_department(self):
        return self.__department

    def get_title(self):
        return self.__title

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def set_department(self, department):
        self.__department = department

    def set_title(self, title):
        self.__title = title

    # __str__ method
    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"ID number: {self.__emp_id}\n"
                f"Department: {self.__department}\n"
                f"Title: {self.__title}")