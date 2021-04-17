def spin_words(sentence):
    res = ""
    words = sentence.split()
    for word in words:
        if len(word) >= 5:
            res += word[::-1]
        else:
            res += word
        res += " "
    return res[:-1]