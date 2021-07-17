import random
numbers = [5, 1, 4, 8, 7, 55, 99, 6]

def verify_sorted(list):
    n = len(list)

    if n <= 1: # Base case
        return True
    return list[0] < list[1] and verify_sorted(list[1:])

def bogo_sort(values):
    count = 0
    while not verify_sorted(values):
        #print("Count : ", count)
        random.shuffle(values)
        count += 1
    print("Attempts: ", count)
    return values

print(bogo_sort(numbers))