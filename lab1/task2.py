import random
from task1 import calc_time


def generate_array(arr_length, arr_range, arr_number):
    array = list()
    for i in range(arr_number):
        array.append([random.randint(0, arr_range) for i in range(arr_length)])
    return array


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        count += 2
        tmp = arr[i]
        j = i - 1
        count += 4
        while j >= 0 and tmp < arr[j]:
            count += 3
            arr[j + 1] = arr[j]
            j = j - 1
            count += 7
        arr[j + 1] = tmp
        count += 4
    # print(f"number of operation: {count}")
    return arr
# 2(n-1)


def hybrid_sort(arr, k):
    if len(arr) < 2:
        return arr
    else:
        middle = int(len(arr) / 2)
        left_arr = merge_sort(arr[:middle])
        right_arr = merge_sort(arr[middle:])

    if len(left_arr) < k:
        left_arr = insertion_sort(left_arr)
    else:
        left_arr = hybrid_sort(left_arr, k)
    if len(right_arr) < k:
        right_arr = insertion_sort(right_arr)
    else:
        right_arr = hybrid_sort(right_arr, k)
    return merge(left_arr, right_arr)


if __name__ == '__main__':
    N = int(input("Array length N = "))
    M = int(input("Max element of array M = "))
    R = int(input("Number of arrays R = "))
    k = 4

    array = generate_array(N, M, R)
    print(f"\ninitial: \n{array}\n")

    calc_time(array, hybrid_sort)

    array = [hybrid_sort(i, k) for i in array]
    print(f"sorted by hybrid (merge and insertion) sort: \n{array}")

    # print(insertion_sort([1, 5, 3, 3, 1, 7, 8, 4, 2, 4]))
