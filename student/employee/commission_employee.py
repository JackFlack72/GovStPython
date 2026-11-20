from employee.employee import Employee


class CommissionEmployee(Employee):
    def __init__(self, name, department, base_pay, commission_earned):
        super().__init__(name, department)
        self.base_pay = base_pay
        self.commission_earned = commission_earned

    def calculate_pay(self):
        return self.base_pay + self.commission_earned

    def get_commission_breakdown(self):
        total = self.calculate_pay()
        pct = (self.commission_earned / total) * 100 if total > 0 else 0.0
        return (
            f"Base ${self.base_pay:.2f} + Commission "
            f"${self.commission_earned:.2f} ({pct:.1f}% of earnings)"
        )

    def __str__(self):
        return f"{self.name} (Commission Employee): ${self.calculate_pay():.2f}"