def binarySearch(arr, search):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == search:
            return mid
        elif arr[mid] > search:
            right = mid - 1
        else:
            left = mid + 1

    return -1


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

assert binarySearch(arr1, 10) == len(arr1) - 2
assert binarySearch(arr2, 100) == -1
