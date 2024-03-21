def write_list_to_file(file_path, my_list):
    """Writes the contents of a list to a file, with each element on a new line."""
    with open(file_path, 'w') as file:
        for element in my_list:
           
            file.write(str(element) + '\n')


file_path = 'output.txt'  
my_list = ['apple', 'banana', 'cherry', 'date']  

write_list_to_file(file_path, my_list)

print(f"List has been written to {file_path}")
