def count_word_frequency(file_path):
    with open(file_path, 'r') as file:
        words = file.read().lower().split()
        
    word_freq = {}
    
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
            
    return word_freq

file_path = 'myfile.txt'  
word_frequencies = count_word_frequency(file_path)

print("Word Frequencies:")
for word, freq in word_frequencies.items():
    print(f"{word}: {freq}")
