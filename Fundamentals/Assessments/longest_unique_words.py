def get_n_longest_unique_words(words, n):
    unique_words = []
    set_words = set(words)

    for unique in set_words:
      unique_words.append(unique)

    return unique_words[:n]


words = [
    "Hello",
    "AlgoExpert",
    "Algo",
    "Testing",
    "Programming",
    "Programming",
    "Coding",
    "Python",
    "JavaScript",
    "Coding",
    "Ruby",
]
n = 5

print(set(words))
print(get_n_longest_unique_words(words, n))
