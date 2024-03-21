#  When will the else part of try-except-else be executed

try:
    print("Trying to convert input to an integer...")
    num = int(input("Enter a number: "))  # This could raise a ValueError
except ValueError:
    print("That was not a valid number.")
else:
    print("You entered a valid number!")
finally:
    print("Execution completed.")
