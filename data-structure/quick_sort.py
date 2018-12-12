""" Implement quick sort in Python.
        Input a list.
        Output a sorted list.
"""
def quicksort(array):
    if len(array) < 2:
        return array
    head, pivot = 0, len(array) - 1
    while head != pivot:
        if array[head] > array[pivot]:
            if head == pivot - 1:
                temp = array[pivot - 1]
                array[pivot - 1] = array[pivot]
                array[pivot] = temp
            else:
                temp = array[pivot - 1]
                array[pivot - 1] = array[pivot]
                array[pivot] = array[head]
                array[head] = temp
            pivot -= 1
        else:
            head += 1
    return quicksort(array[:pivot]) + [array[pivot]] + quicksort(array[pivot + 1:])

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# test = [21, 4]
# print test[:1]
print quicksort(test)
