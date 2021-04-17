def get_middle(s):
    length = len(s)
    if length % 2:
        return s[(length - 1) // 2]
    else:
        return s[(length // 2) - 1] + s[length // 2]