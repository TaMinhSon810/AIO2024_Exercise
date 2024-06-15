def word_count(file_path):
    words = file_path.split()

    counter = {}

    for i in words:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1

    print(counter)

!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
file_path = "/content/P1_data.txt"
word_count(file_path)