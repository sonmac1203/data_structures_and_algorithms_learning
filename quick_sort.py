def quick_sort(values):
    if len(values) <= 1:
        return values
    pivot = values[0]
    less_than_pivot = []
    greater_than_pivot = []
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

numbers = [5, 2, 6, 7, 9, 4, 435, 77, 547]
print(numbers)
print(quick_sort(numbers))