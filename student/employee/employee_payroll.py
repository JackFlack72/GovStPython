from employee.employee import Employee
from employee.hourly_employee import HourlyEmployee
from employee.salary_employee import SalaryEmployee
from employee.commission_employee import CommissionEmployee


def load_employees():
    employees = [
        HourlyEmployee("Nick DeFalco", "Sales", 25.0, 2080),
        SalaryEmployee("Applejack Johnson", "Sales", 44000.0),
        SalaryEmployee("Mario Dubois", "Sales", 77200.0),
        SalaryEmployee("Anthony Jo", "Engineering", 98000.0),
        Employee("Stephanie Johnson", "Engineering"),
        CommissionEmployee("Dominic Togo", "Maintenance", 20000.0, 45000.0),
        HourlyEmployee("Christina Gonzalez", "Maintenance", 19.8, 2080),
        HourlyEmployee("Geoffrey Dav", "HR", 65.0, 2080),
    ]
    employees[4].calculate_pay = lambda: 31200.0
    return employees


def main():
    employees = load_employees()

    # Group employees into a dictionary keyed by department
    employee_dict = {}
    for emp in employees:
        if emp.department not in employee_dict:
            employee_dict[emp.department] = []
        employee_dict[emp.department].append(emp)

    for department, emp_list in employee_dict.items():
        print(f"Department: {department}")
        total_payroll = 0.0

        for emp in emp_list:
            pay = emp.calculate_pay()
            total_payroll += pay
            print(emp)

            # Only CommissionEmployee has a base vs. commission breakdown
            if isinstance(emp, CommissionEmployee):
                print(emp.get_commission_breakdown())

        print(f"Total Payroll: ${total_payroll:.2f}")


if __name__ == "__main__":
    main()