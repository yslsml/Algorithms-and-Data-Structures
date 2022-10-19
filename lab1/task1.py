import random
from time import process_time


def generate_array(arr_length, arr_range, arr_number):
    array = list()
    for i in range(arr_number):
        array.append([random.randint(0, arr_range) for i in range(arr_length)])
    return array


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        q = random.choice(arr)
    lower_arr = [n for n in arr if n < q]
    equal_arr = [q] * arr.count(q)
    greater_arr = [n for n in arr if n > q]
    return quick_sort(lower_arr) + equal_arr + quick_sort(greater_arr)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and tmp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = tmp
    return arr


def hybrid_sort(arr, k):
    if len(arr) < 2:
        return arr
    else:
        q = random.choice(arr)
    lower_arr = [n for n in arr if n < q]
    equal_arr = [q] * arr.count(q)
    greater_arr = [n for n in arr if n > q]

    if len(lower_arr) < k:
        lower_arr = insertion_sort(lower_arr)
    else:
        lower_arr = hybrid_sort(lower_arr, k)
    if len(greater_arr) < k:
        greater_arr = insertion_sort(greater_arr)
    else:
        greater_arr = hybrid_sort(greater_arr, k)
    return lower_arr + equal_arr + greater_arr


def calc_time(array, func):
    best_time = None
    best_k = 0
    for k in range(len(array[0]) // 2 + 1):
        sum = 0
        print(f"k = {k}")
        for arr in array:
            print(f"\t{arr}")
            start = process_time()
            func(arr, k)
            print(f"\t{func(arr, k)}")
            end = process_time()
            time = end - start
            print("\trun time = {:,.10f}\n".format(time))
            sum += time
        if not best_time:
            best_time = sum
            best_k = k
        if sum < best_time:
            best_time = sum
            best_k = k
        print("k = {:d}\tsum time = {:,.10f}\n".format(k, sum))
    print("best k = {:d} , best time = {:,.10f}".format(best_k, best_time))


if __name__ == '__main__':
    N = int(input("Array length N = "))
    M = int(input("Max element of array M = "))
    R = int(input("Number of arrays R = "))
    k = 4

    array = generate_array(N, M, R)
    print(f"\ninitial: \n{array}\n")

    calc_time(array, hybrid_sort)

    array = [hybrid_sort(i, k) for i in array]
    print(f"\nsorted by hybrid (quick and insertion) sort: \n{array}")
