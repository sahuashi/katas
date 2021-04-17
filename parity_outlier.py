def find_outlier(integers):
    even = [num for num in integers if num % 2 == 0]
    odd = [num for num in integers if num % 2]
    return odd[0] if len(even) > len(odd) else even[0]