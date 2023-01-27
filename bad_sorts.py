"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import time
#import matplotlib.pyplot as plt


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L:list, i:int, j:int):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return


# This is the optimization/improvement we saw in lecture
def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L, i)


def insert2(L, i):
    value = L[i]
    while i > 0:
        if L[i - 1] > value:
            L[i] = L[i - 1]
            i -= 1
        else:
            L[i] = value
            return
    L[0] = value


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

def bubble_sort2(L:list):
    for _ in range(len(L)):
        i = 0
        value = L[i]
        while i < len(L) - 1:
            if L[i+1] < value:
                L[i] = L[i+1]
            else:
                L[i] = value
                value = L[i+1]
            i += 1
        L[len(L)-1] = value
            


# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

# ******************* Testing *******************

'''
test = create_random_list(10,20)
print(test)
bubble_sort2(test)
print(test)
'''


experiments = 1000
list_size = 100
max_val = 500

#bubble_sort testing
total_time = 0
for _ in range(experiments):
    before = time.perf_counter()

    rand_list = create_random_list(list_size,max_val)
    bubble_sort(rand_list)

    after = time.perf_counter()
    total_time += (after - before)
print(f"average time to run bubble_sort on a list of size {list_size} {experiments} times: {total_time/experiments}")


#bubble_sort2 testing
total_time = 0
for _ in range(experiments):
    before = time.perf_counter()

    rand_list = create_random_list(list_size,max_val)
    bubble_sort2(rand_list)

    after = time.perf_counter()
    total_time += (after - before)
print(f"average time to run bubble_sort2 on a list of size {list_size} {experiments} times: {total_time/experiments}")