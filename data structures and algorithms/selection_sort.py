# Implementing selection sort
def selection(unsorted):
    '''Sorts and returns the sorted list'''
    for i in range(len(unsorted)):
        # mini = unsorted[i]
        ind = i
        for j in range(i, len(unsorted)):
            if unsorted[i] > unsorted[j]:
                # mini = unsorted[j]
                ind = j
        unsorted[i], unsorted[ind] = unsorted[ind], unsorted[i]
    return unsorted

print(selection([5, 4, 2, 1, 2000, 2312, 6]))
print(selection([9, 8, 7, 6, 5, 4, 3]))
selection([list(range(100000000, 0, -1))])
