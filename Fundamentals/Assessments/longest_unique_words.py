def get_n_longest_unique_words(words, n):
    unique_words = get_unique_words(words)
    sorted_words = sorted(unique_words, key=len, reverse=True)
    return sorted_words[:n]


def get_unique_words(words):
    unique_words = []
    for word in words:
        if words.count(word) == 1:
            unique_words.append(word)

    return unique_words
