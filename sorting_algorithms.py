

import random
import copy
import time
import os

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, pi+1, high)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
arrSizes = [[10, 10000, 100000]]
arrTypes = ["Random", "Sorted", "Reverse Sorted", "Partially Sorted"]
for sizes in arrSizes:
    print("Input size:", sizes)
    for arrType in arrTypes:
        print("Input size:", sizes)
        print("Input type:", arrType)
        for size in sizes:
            if arrType == "Random":
                arr = [random.randint(0, 1000) for _ in range(size)]
            elif arrType == "Sorted":
                arr = list(range(size))
            elif arrType == "Reverse Sorted":
                arr = list(range(size, 0, -1))
            elif arrType == "Partially Sorted":
                arr = list(range(size))
                for _ in range(size // 10):
                    idx1, idx2 = random.randint(0, size - 1), random.randint(0, size - 1)
                    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
            arrCopy1 = copy.deepcopy(arr)
            startTime1 = time.time()
            mergeSort(arrCopy1)
            endTime1 = time.time()
            duration1 = (endTime1 - startTime1) * 1000  # Time in milliseconds
            arrCopy2 = copy.deepcopy(arr)
            startTime2 = time.time()
            quickSort(arrCopy2, 0, len(arrCopy2) - 1)
            endTime2 = time.time()
            duration2 = (endTime2 - startTime2) * 1000  # Time in milliseconds
            arrCopy3 = copy.deepcopy(arr)
            startTime3 = time.time()
            heapSort(arrCopy3)
            endTime3 = time.time()
            duration3 = (endTime3 - startTime3) * 1000  # Time in milliseconds
            print(f"Input size: {size}")
            print(f"Merge Sort - Time: {duration1} ms")
            print(f"Quick Sort - Time: {duration2} ms")
            print(f"Heap Sort - Time: {duration3} ms")
            print()
