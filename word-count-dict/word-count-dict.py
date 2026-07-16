def word_count_dict(sentences):
    word_freq = {}
    for sentence in sentences:
        for word in sentence:
            word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq