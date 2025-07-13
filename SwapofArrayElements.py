# Swap Of elemnets using Recursion in Array in Python .
import array


def swap(arr: array.array, i: int, n: int):
    if i >= n // 2:
        return
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    swap(arr, i+1, n)


array_l = array.array('i', [1, 2, 3, 4, 5, 6])
Array_length = len(array_l)
swap(array_l, 0, Array_length)
# .' '.join(map(str,array_l)) converts array elements to string and joins them with space
print(' '.join(map(str, array_l)))
# Output: 6 5 4 3 2 1
