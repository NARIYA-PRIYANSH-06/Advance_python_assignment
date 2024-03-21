def read_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        
        lines = file.readlines()
        
        last_n_lines = lines[-n:]
        
        for line in last_n_lines:
            print(line, end='')

file_path = 'myfile.txt'  
n = 1 
read_last_n_lines(file_path, n)
