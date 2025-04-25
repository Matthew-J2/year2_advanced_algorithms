"""
len():
https://docs.python.org/3/reference/datamodel.html#object.__len__
len() time complexity:
https://antonz.org/list-internals/
"""

import time

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
def main():
    start = time.time()
    print(selection_sort2([3, 8, 12, -4, 3, 6, 5, 1, 0, 7, 2, 5, 4, -5, -2, 0.7, 7]))
    end = time.time()
    print(end - start)
if __name__ == "__main__":
    main()
