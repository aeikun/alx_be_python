FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_temperature(temperature, unit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR, CELSIUS_TO_FAHRENHEIT_FACTOR
    
    if unit.upper() == 'F':
        celsius = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        return celsius, 'C'
    elif unit.upper() == 'C':
        fahrenheit = temperature * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
        return fahrenheit, 'F'
    else:
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

def main():
    try:
        temperature_str = input("Enter the temperature to convert: ")
        temperature = float(temperature_str)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip()

        converted_temp, target_unit = convert_temperature(temperature, unit)

        print(f"{temperature}°{unit.upper()} is {converted_temp}°{target_unit}")

    except ValueError as ve:
        print(f"Error: {ve}. Please enter a numeric value for temperature.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
