
file_name = "myfile.txt"


text_to_append = "\nThis is the new text we're appending."


with open(file_name, "a") as file:
    file.write(text_to_append)


with open(file_name, "r") as file:
    content = file.read()
    print("Updated file content:")
    print(content)
