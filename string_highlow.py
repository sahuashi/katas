def high_and_low(numbers):
    nums = [int(num) for num in numbers.split()]
    highest = max(nums)
    lowest = min(nums)
    numbers = f"{highest} {lowest}"
    return numbers