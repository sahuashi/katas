def digital_root(n):
    # base case
    if len(str(n))==1:
        return n
    # recursive case
    sum = 0
    nums = [int(x) for x in str(n)]
    for i in nums:
        sum += i  
    return digital_root(sum)
