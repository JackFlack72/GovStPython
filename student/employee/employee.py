class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def calculate_pay(self):
        return 0.0

    def __str__(self):
        return f"{self.name} (Employee): ${self.calculate_pay():.2f}"