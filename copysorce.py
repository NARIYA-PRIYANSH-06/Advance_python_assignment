# Step 1: Open the source file and read its content
with open('myfile.txt', 'r') as source_file:
    content = source_file.read()

# Step 3 and 4: Open the destination file in write mode and write the content
with open('output.txt', 'w') as destination_file:
    destination_file.write(content)

print("Content copied successfully.")
