def square_digits(num):
    nums = [int(digit) for digit in str(num)]
    squared = [x**2 for x in nums]
    return int(''.join(str(number) for number in squared))