from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_datetime = datetime.now()

    # Get the current date and time
    current_date = current_datetime.date()

    # Formatting the date and time
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

def calculate_future_date():
    # Prompt the user to enter a number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Get the current date
    current_date = datetime.now().date()
    
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    
    # Print the future date in a readable format
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {future_date}")


def main():
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()