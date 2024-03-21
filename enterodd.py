class EvenNumberException(Exception):
    def __init__(self, message="Even numbers are not allowed"):
        self.message = message
        print(EvenNumberException(Exception))

try:
    number = int(input("Please enter an odd number: "))
    if number % 2 == 0: 
        raise EvenNumberException
    else:
        print("Thank you for entering an odd number!")
except ValueError:
    print("That's not an integer!")
except EvenNumberException as e:
    print(e)
