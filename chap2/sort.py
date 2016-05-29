import random

def swap(a, x, y):
    a[x], a[y] = a[y], a[x]

def selection_sort(a):
    "Selection Sort in-place"
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        swap(a, i, min_idx)
    return a
