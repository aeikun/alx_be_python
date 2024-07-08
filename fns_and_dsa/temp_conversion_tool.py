FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip()

        if unit.upper() == 'F':
            converted_temp = convert_to_celsius(temperature)
            target_unit = 'C'
        elif unit.upper() == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            target_unit = 'F'
        else:
            print("Invalid temperature unit. Please enter 'C' or 'F'.")

        print(f"{temperature}°{unit.upper()} is {converted_temp}°{target_unit}")


if __name__ == "__main__":
    main()
