# Absolute zero in Celsius is -273.15
ABSOLUTE_ZERO = -273.15

# Input Validation Loop
celsius_limit = float(input("Enter a Celsius temperature to convert up to: "))

while celsius_limit < ABSOLUTE_ZERO:
    print(f"Error: Temperature cannot be below absolute zero ({ABSOLUTE_ZERO}°C).")
    celsius_limit = float(input("Enter a Celsius temperature to convert up to: "))

# Output Header
print()
print("Celsius\tFahrenheit")
print("-------------------")

# Loop from 0 up to user input
current_celsius = 0
while current_celsius <= celsius_limit:
    fahrenheit = (current_celsius * 9 / 5) + 32
    print(f"{current_celsius}\t{fahrenheit:.2f}")
    current_celsius += 1