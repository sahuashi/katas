def persistence(n):
    if(len(str(n)) == 1): return 0
    counter, product = 0, 1
    while len(str(n)) > 1:
        digits = [int(x) for x in str(n)]
        for digit in digits:
            product *= digit
        counter += 1
        n = product
        product = 1
    return counter