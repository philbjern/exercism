from collections import Counter


def find_anagrams(word, candidates):
    word_counter = Counter(word.lower())
    anagrams = []

    for candidate in candidates:
        if candidate.lower() == word.lower():
            continue

        candidate_counter = Counter(candidate.lower())
        if word_counter == candidate_counter:
            anagrams.append(candidate)

    print(anagrams)
    return anagrams


if __name__ == '__main__':
    find_anagrams('listen', ['enlists', 'google', 'inlets', 'banana'])
