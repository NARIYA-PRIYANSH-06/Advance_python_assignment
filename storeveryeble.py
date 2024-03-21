def file_to_string(file_path):
    """Reads a file line by line and stores it into a string variable."""
    with open(file_path, 'r') as file:
        content = ""
        for line in file:
            content += line
    return content

file_path = 'myfile.txt'  
file_content = file_to_string(file_path)
print("File content:")
print(file_content)
