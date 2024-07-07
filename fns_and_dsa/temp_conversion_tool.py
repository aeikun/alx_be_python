def convert_to_celsius(fahrenheit):
    fahrenheit_to_celsius_factor = 5 / 9
    celsius = (fahrenheit - 32) * fahrenheit_to_celsius_factor
    return celsius

def convert_to_fahrenheit(celsius):
    celsius_to_fahrenheit_factor = 9 / 5
    fahrenheit = celsius * celsius_to_fahrenheit_factor + 32
    return fahrenheit

def convert_temperature(temperature, unit):
    if unit.upper() == 'F':
        converted_temp = convert_to_celsius(temperature)
        target_unit = 'C'
    elif unit.upper() == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        target_unit = 'F'
    else:
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
    
    return converted_temp, target_unit

def main():
    try:
        temperature_str = input("Enter the temperature to convert: ")
        temperature = float(temperature_str)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip()

        converted_temp, target_unit = convert_temperature(temperature, unit)

        print(f"{temperature:.2f}°{unit.upper()} is {converted_temp:.2f}°{target_unit}")

    except ValueError as ve:
        print(f"Error: {ve}. Please enter a numeric value for temperature.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()