# Implementing insertion sort
def insertion(unsorted):
    '''Sorts and returns the sorted list'''
    for i in range(1, len(unsorted)):
        ind = i
        insert = unsorted[i]
        for j in range(i-1, -1, -1):
            if unsorted[i] < unsorted[j]:
                insert = unsorted[i]
                ind = j
        unsorted[ind+1:i+1] = unsorted[ind:i]
        unsorted[ind] = insert
    return unsorted


print(insertion([5, 4, 2, 1, 2000, 2312, 6]))
print(insertion([9, 8, 7, 6, 5, 4, 3]))
insertion([list(range(10000000, 0, -1))])
