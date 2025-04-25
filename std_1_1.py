"""
len():
https://docs.python.org/3/reference/datamodel.html#object.__len__
len() time complexity:
https://antonz.org/list-internals/
"""

import time

def selection_sort1(arr):
    """For each pass over the list to be sorted, sets the initial minimum value for a pass,
    values below the minimum have been sorted.
    For each item in the list over the current minimum, check if the item's value is lower
    than the minimum.
    After finding the minimum for a pass, swap it into the position corresponding to the pass."""

    for i in range(len(arr)-1):
        minimum = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
                print(minimum)
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr

def selection_sort2(arr):
    """In this version of the function, the end of the list is found before the for loop using len()
    This significantly reduces overhead because len() is not called every time the inner for loop is started
    For example in a list of size 7, len() is called once instead of 7 times."""
    length = len(arr)
    for i in range(length -1):
        minimum = i
        for j in range(i+1, length):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr

#def selection_sort2(arr):
#    print(arr[:-1])
#    for idx, i in enumerate(arr[:-1]):
#        minimum = idx
#        for idx2, j in enumerate(arr, idx-1):
#            print("a")
#            if arr[idx2] < arr[minimum]:
#                minimum = idx2
#        arr[idx], arr[minimum] = arr[minimum], arr[idx]
#    return arr

"""def selection_sort2(arr):
    for idx, i in enumerate(arr):
        if idx == 0:
            continue
        minimum = idx - 1
        for idx2, j in enumerate(arr[idx-1:]):
            print(idx2, minimum, j)
            if arr[idx2] < arr[minimum]:
                minimum = j
        arr[idx], arr[minimum] = arr[minimum], arr[idx]
        print("")
    return arr
"""
def main():
    start = time.time()
    print(selection_sort1([3,  8, 12, -4, 3, 6, 5, 1, 0, 7, 2, 5, 4, -5, -2, 0.7, 7]))
    end = time.time()
    print("Time taken:", end - start)
    print(time.time())
    start = time.time()
    print(selection_sort2([3, 8, 12, -4, 3, 6, 5, 1, 0, 7, 2, 5, 4, -5, -2, 0.7, 7]))
    end = time.time()
    print("Time taken", end - start)
if __name__ == "__main__":
    main()