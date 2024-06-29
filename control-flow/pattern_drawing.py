pattern = int(input("Enter the size of the pattern: "))


if pattern <= 0:
    print("Please enter a positive integer.")

else:
    row = 0


while row < pattern:
    for col in range(pattern):
        print("*", end="")
    
    print()

    row += 1