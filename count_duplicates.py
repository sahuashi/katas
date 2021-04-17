from collections import Counter
def duplicate_count(text):
    text = text.lower()
    count = Counter(text)
    return len([x for x in count.values() if x > 1])