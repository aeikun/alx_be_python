# multiplication_table.py

def print_multiplication_table():
    try:
        # Prompt the user to enter a number
        number = int(input("Enter a number to see its multiplication table: "))
        
        # Generate and print the multiplication table from 1 to 10
        for i in range(1, 11):
            product = number * i
            print(f"{number} * {i} = {product}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Run the function to print the multiplication table
if __name__ == "__main__":
    print_multiplication_table()