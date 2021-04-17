def accum(s):
    res, counter = "", 0
    for char in s:
        counter += 1
        for i in range(counter):
            if res.endswith("-") or counter == 1: res += char.upper()
            else: res += char.lower()
        res += "-"
    return res[:-1]