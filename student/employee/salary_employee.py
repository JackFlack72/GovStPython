from employee.employee import Employee


class SalaryEmployee(Employee):
    def __init__(self, name, department, annual_salary):
        super().__init__(name, department)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary

    def __str__(self):
        return f"{self.name} (Salaried Employee): ${self.calculate_pay():.2f}"