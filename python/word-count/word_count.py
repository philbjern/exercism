import re

def count_words(sentence):
    word_counts = {}
    text = sentence.lower()
    words = re.findall(r'\w+|\d+', text)

    for word in words:
        if '_' in word:
            for word1 in word.split('_'):
                word_counts[word1] = word_counts.get(word1, 0) + 1
        else:
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


if __name__ == "__main__":
    print(count_words("\"That's the password: 'PASSWORD 123'!\", cried the Special Agent.\nSo I fled."))
    print(count_words("can, can't, can't"))
