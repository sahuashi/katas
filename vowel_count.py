def get_count(input_str):
    num_vowels = 0
    for x in range(len(input_str)):
        if input_str[x] in {'a', 'e', 'i', 'o', 'u'}:
            num_vowels += 1
    return num_vowels