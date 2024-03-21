def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

file_path = 'myfile.txt'
number_of_lines = count_lines_in_file(file_path)
print(f"The file has {number_of_lines} lines.")
