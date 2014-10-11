# Implementing bubble sort
def bubble(unsorted):
    '''Sorts and returns the sorted list'''
    for i in range(len(unsorted)):
        swap = 0
        for j in range(1, len(unsorted)):
            if unsorted[j-1] > unsorted[j]:
                unsorted[j-1], unsorted[j] = unsorted[j], unsorted[j-1]
                swap = 1
        if swap == 0:
            break
    return unsorted


print(bubble([5, 4, 2, 1, 2000, 2312, 6]))
print(bubble([9, 8, 7, 6, 5, 4, 3]))
bubble([list(range(10000000, 0, -1))])
