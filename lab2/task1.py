import math
import random
from lab1.task1 import quick_sort

def generate_array(arr_length, arr_range, arr_number=1):
    array = list()
    for i in range(arr_number):
        arr = [random.randint(0, arr_range) for i in range(arr_length)]
        array.append(quick_sort(arr))
    return array


def binary_search(array, key):
    count_operations = 0
    left = 0
    right = len(array) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if key == array[mid]:
            count_operations += 1
            print(f"\n[Number of comparison operations in binary search is {count_operations}]")
            index = mid
            return index
        if key < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
        count_operations += 2
    print(f"\n[Number of comparison operations in binary search is {count_operations}]")
    return index


def interpolation_search(array, key):
    count_operations = 0
    left = 0
    right = len(array) - 1
    while left <= right and array[left] <= key <= array[right]:
        index = left + int(((float(right - left) / (array[right] - array[left])) * (key - array[left])))
        if array[index] == key:
            count_operations += 1
            print(f"[Number of comparison operations in interpolation search is {count_operations}]")
            return index
        if array[index] < key:
            left = index + 1
        else:
            right = index - 1
        count_operations += 2
    print(f"[Number of comparison operations in interpolation search is {count_operations}]")
    return -1


if __name__ == '__main__':
    N = int(input("Array length N = "))
    M = int(input("Max element of array M = "))
    R = int(input("Number of arrays R = "))

    array = generate_array(N, M, R)

    for arr in array:
        key = random.randint(0, M)
        res_binary = binary_search(arr, key)
        res_interp = interpolation_search(arr, key)
        print(f"Array: \n{arr}\nThe desired element: {key}\nResult (index of element) in binary search: {res_binary} \n"
              f"Result (index of element) in interpolation search: {res_interp}\n")




