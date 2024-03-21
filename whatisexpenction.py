'''
Exception Handling
Exception handling is a crucial concept in programming that involves managing errors and unusual conditions that occur during the execution of a program. The main goal of exception handling is to allow the program to continue running or gracefully terminate, even if an error occurs. This prevents the program from crashing unexpectedly and allows for a more robust and user-friendly application.

In Python, exception handling is achieved through the use of try, except, else, and finally blocks:

try Block: You start by wrapping the code that might cause an exception in a try block. Python attempts to execute this code normally.

except Block: If an exception occurs in the try block, the control is passed to the except block. You can specify different except blocks for different types of exceptions, allowing for specific responses to different errors.

else Block: If no exceptions occur in the try block, the else block is executed. This block is optional and is used for code that should run only when the try block is successful and no exceptions were raised.

finally Block: This block is executed no matter what, whether an exception is raised or not. It's typically used for cleaning up resources, like closing files or releasing external resources. The finally block is optional as well.'''


#**************************************************************
#**************************************************************

'''What is an Error in Python?
In Python, an error is a broad term for any problematic condition that arises during the execution of a program. Errors in Python can be broadly classified into two categories:

Syntax Errors: These are errors detected by Python as it parses your code. They occur when the code does not conform to the syntax rules of Python. For example, missing a colon at the end of an if statement or not closing parentheses. Syntax errors prevent the program from being executed.

Exceptions: These are errors detected during execution. Unlike syntax errors, exceptions could occur even if the code is syntactically correct. Exceptions arise from unforeseen situations during execution, such as trying to open a file that does not exist, dividing by zero, or trying to access a list element that is out of range.

'''