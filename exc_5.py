def process_word(word):
    vowels = ['a', 'e', 'i', 'u', 'o', 'y']
    prefix = 'y'
    postfix = 'cat'
    for i in word:
        if i in vowels:
            return word.replace(word[0], prefix)
        else:
            tmp_prefix = word[0]
            return word[1:] + tmp_prefix + postfix


def process_phrase(inp):
    words = inp.split()
    result_string = ""
    for i in words:
        result_string += process_word(i) + " "
    return result_string


user_input = input('Enter your word: ')
print(process_phrase(user_input))
