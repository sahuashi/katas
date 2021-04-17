from collections import Counter
def find_it(seq):
    count = Counter(seq)
    print(count.items())
    nums = [key for key,value in count.items() if value%2==1]
    return nums[0]