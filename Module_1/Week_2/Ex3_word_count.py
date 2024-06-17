def word_count(file_path):
    with open(file_path, 'r') as f:
        document = f.read().lower()

    words = document.split()

    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter

file_path = "AIO2024_Exercise/Module_1/Week_2/P1_data.txt"
print(word_count(file_path))