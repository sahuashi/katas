def maskify(cc):
    cc = list(cc)
    length = len(cc)
    for i in range(length-4):
        cc[i] = '#'
    cc = ''.join(cc)
    return cc