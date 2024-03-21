def read_first_n_lines(file_name, n):
    
    with open(file_name, 'r') as file:
        for i in range(n):
            line = file.readline()
            print(line.strip())  


file_name = 'myfile.txt'  
n=1
read_first_n_lines(file_name, n)
