# constants for absolute zero
ABSOLUTE_ZERO_FAHRENHEIT = -459.67
ABSOLUTE_ZERO_CELSIUS = -273.15

# display menu options
print("Temperature Conversion Options:")
print("1. Convert Fahrenheit to Celsius")
print("2. Convert Celsius to Fahrenheit")

choice = input("Enter your choice (1 or 2): ")

# fahrenheit to celsius conversion
if choice == '1':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # input validation
    if fahrenheit < ABSOLUTE_ZERO_FAHRENHEIT:
        print(f"Error: Temperature cannot be below absolute zero ({ABSOLUTE_ZERO_FAHRENHEIT:.2f}°F).")
    else:
        celsius = (fahrenheit - 32) * (5 / 9)
        print(f"{fahrenheit:.1f} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")

# celsius to fahrenheit conversion
elif choice == '2':
    celsius = float(input("Enter temperature in Celsius: "))
    
    # input validation
    if celsius < ABSOLUTE_ZERO_CELSIUS:
        print(f"Error: Temperature cannot be below absolute zero ({ABSOLUTE_ZERO_CELSIUS:.2f}°C).")
    else:
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius:.1f} degrees Celsius is {fahrenheit:.2f} degrees Fahrenheit.")

else:
    print("Error: Invalid choice option selected.")