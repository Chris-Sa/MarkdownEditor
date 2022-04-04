def choose_vowels(letters):
    vowels = ['a', 'e', 'i', 'u', 'o']
    new_list = list(filter(lambda x: x in vowels, letters))
    return new_list