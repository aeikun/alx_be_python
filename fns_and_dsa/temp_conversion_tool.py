def convert_to_celsius(fahrenheit):
    fahrenheit_to_celsius_factor = 5 / 9
    celsius = (fahrenheit - 32) * fahrenheit_to_celsius_factor
    return celsius

def convert_to_fahrenheit(celsius):
    celsius_to_fahrenheit_factor = 9 / 5
    fahrenheit = celsius * celsius_to_fahrenheit_factor + 32
    return fahrenheit

def main():
    
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            print("Invalid temperature unit. Please enter 'C' or 'F'.")
    

if __name__ == "__main__":
    main()
