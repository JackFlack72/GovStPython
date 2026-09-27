# Validate Monthly Investment
while (monthly_investment := float(input("Enter monthly investment: "))) <= 0:
    print("Error: Must be a positive number.")

# Validate Yearly Interest Rate
while (yearly_interest_rate := float(input("Enter yearly interest rate (e.g., 5 for 5%): "))) <= 0:
    print("Error: Must be a positive number.")

# Validate Investment Years
while (investment_years := int(input("Enter investment years: "))) <= 0:
    print("Error: Must be a positive integer.")

# Setup Variables For Calculation
total_months = investment_years * 12
monthly_rate = (yearly_interest_rate / 100) / 12
total_balance = 0.0

print()
print("Month\tMonthly Revenue\tTotal Balance")
print("-------------------------------------")

# Process Month By Month
for month in range(1, total_months + 1):
    total_balance += monthly_investment
    monthly_revenue = total_balance * monthly_rate
    total_balance += monthly_revenue
    print(f"{month}\t${monthly_revenue:.2f}\t\t${total_balance:.2f}")

print("-------------------------------------")
print(f"Total Balance after {investment_years} years: ${total_balance:.2f}")