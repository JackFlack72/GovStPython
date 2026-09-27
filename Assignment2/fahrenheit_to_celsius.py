# prompt the user for a temperature in Fahrenheit
fahrenheit = float(input('Enter the temperature in Fahrenheit: '))

# perform the conversion to Celsius
celsius = (fahrenheit - 32) * (5 / 9)

# generate the output using f-string to format the result
print(f'{fahrenheit:.1f} degrees Fahrenheit is {celsius:.2f} degrees Celsius')