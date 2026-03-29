import random
import time

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

def measure_time(func, arr, target=None):
    start = time.time()
    if target is not None:
        func(arr, target)
    else:
        func(arr)
    end = time.time()
    return end - start

sizes = [100, 500, 1000, 2000]

print("\nAlgorithm Performance Analysis\n")

for size in sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]
    target = arr[random.randint(0, size - 1)]

    print("Dataset Size:", size)

    t1 = measure_time(bubble_sort, arr)
    print("Bubble Sort:", t1)

    t2 = measure_time(selection_sort, arr)
    print("Selection Sort:", t2)

    t3 = measure_time(merge_sort, arr)
    print("Merge Sort:", t3)

    t4 = measure_time(linear_search, arr, target)
    print("Linear Search:", t4)

    sorted_arr = sorted(arr)
    t5 = measure_time(binary_search, sorted_arr, target)
    print("Binary Search:", t5)

    print("-" * 40)