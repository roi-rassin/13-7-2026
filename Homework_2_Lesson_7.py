# Start

number = int(input("Enter a number, if you want a stop enter 999: "))
new_number = 0

while number != 999:
    new_number = new_number + number
    number = int(input("Enter a number, if you want a stop enter 999: "))

print(f"\nYour sum is {new_number}!")

# Stop