def character_count(word):
    character_statistic = {}

    for i in range(len(word)):
        char = word[i]
        if char not in character_statistic:
            character_statistic[char] = 1
        else:
            character_statistic[char] += 1
    
    print(character_statistic)

character_count('smiles')