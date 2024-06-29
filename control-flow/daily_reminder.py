task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

reminder = f"'{task}' is a {priority} priority task"

match priority:
        case "high":
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            else:
                reminder += ". Consider completing it as soon as possible."
        case "medium":
            if time_bound == "yes":
                reminder += " that should be done today."
            else:
                reminder += ". Try to complete it soon."
        case "low":
            if time_bound == "yes":
                reminder += " that you should aim to complete today."
            else:
                reminder += ". Consider completing it when you have free time."
        case _:
            reminder = "Invalid priority level. Please enter high, medium, or low."

print(f"\nReminder: {reminder}")