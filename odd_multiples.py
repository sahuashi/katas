def solution(number):
    multiples = set()
    sum = 0
    for i in range(number):
        if (i % 3 == 0 or i % 5 == 0):
            multiples.add(i)
    for num in multiples:
        sum += num
    return sum