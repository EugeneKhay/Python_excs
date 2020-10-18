def process_word(word):
    if word[0] in ['a', 'e', 'i', 'u', 'o']:
        return word + 'way'
    return word[1:] + word[0] + 'ay'


def process_two_vowels(word):
    first_vowel = None
    for i in word:
        if i in ['a', 'e', 'i', 'u', 'o']:
            if i != first_vowel and first_vowel != None:
                return word + 'way'
            first_vowel = i
    return word[1:] + word[0] + 'ay'


def process_three_vowels(word):
    counter = 0
    for i in word:
        if i in ['a', 'e', 'i', 'u', 'o']:
            counter += 1
            if counter == 3:
                return word + 'way'
    return word[1:] + word[0] + 'ay'


def process_phrase(inp):
    result_string = []
    for i in inp.split():
        result_string.append(process_word(i))
    return " ".join(result_string)


user_input = input('Enter your word: ')
print(process_phrase(user_input))
