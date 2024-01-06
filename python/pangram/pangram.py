def is_pangram(sentence):
    alphabet_letters = ['a', 'b', 'c', 'd',
                        'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'l',
                        'm', 'n', 'o', 'p',
                        'u', 'v', 'w', 'x',
                        'y', 'z']

    sentence_letters = [letter.lower() for letter in sentence.strip() if letter.isalpha()]

    return set(sentence_letters) >= set(alphabet_letters)
