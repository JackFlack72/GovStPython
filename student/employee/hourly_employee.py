from employee.employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, name, department, hourly_rate, hours_worked):
        super().__init__(name, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"{self.name} (Hourly Employee): ${self.calculate_pay():.2f}"