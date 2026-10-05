# Temperature_conversion.py
# Refactored temperature conversion program built using the provided function skeleton.


# Global Constants
CELSIUS = "C"
FAHRENHEIT = "F"


def main():
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)


def get_temperature_type():
    # Prompts user for temperature type (C or F) until valid input is received
    while True:
        unit = input("Enter temperature type (C for Celsius, F for Fahrenheit): ").strip().upper()
        if unit in (CELSIUS, FAHRENHEIT):
            return unit
        print("Invalid input! Please enter 'C' or 'F'.")


def get_temperature(temperature_type):
    # Prompts user for numeric temperature value until valid input is received
    unit_name = "Celsius" if temperature_type == CELSIUS else "Fahrenheit"
    while True:
        try:
            return float(input(f"Enter temperature in {unit_name}: "))
        except ValueError:
            print("Invalid input! Please enter a valid numerical value.")


def display_conversion(temperature_type, temperature):
    # Performs conversion and displays the formatted result
    if temperature_type == CELSIUS:
        convertedTemp = (temperature * 9 / 5) + 32
        print(f"\n{temperature:.1f}° Celsius is equal to {convertedTemp:.1f}° Fahrenheit.")
    else:
        convertedTemp = (temperature - 32) * 5 / 9
        print(f"\n{temperature:.1f}° Fahrenheit is equal to {convertedTemp:.1f}° Celsius.")


if __name__ == "__main__":
    main()