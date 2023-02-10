"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import time
import matplotlib.pyplot as plt


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
def bubble_sort(L:list):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

#implements "optimizations" similar to insertion_sort2
def bubble_sort2(L:list):
    for _ in range(len(L)):
        i = 0
        value = L[i]
        while i < len(L) - 1:
            next = L[i+1]
            if next < value:
                L[i] = next
            else:
                L[i] = value
                value = next
            i += 1
        L[len(L)-1] = value


#same as bubble_sort2 but with a clause that breaks early if the list is sorted
def bubble_sort3(L:list):
    for _ in range(len(L)):
        i = 0
        sorted = True
        value = L[i]
        while i < len(L) - 1:
            next = L[i+1]
            if next < value:
                L[i] = next
                if sorted == True:
                    sorted = False
            else:
                L[i] = value
                value = next
            i += 1
        L[len(L)-1] = value
        if sorted == True:
            break
            


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

def find_max_index(L, n):
    max_index = n
    for i in range(n+1, len(L)):
        if L[i] > L[max_index]:
            max_index = i
    return max_index

def selection_sort2(L):
    i=0
    j=len(L)-1
    while(i < j):
        min_index = find_min_index(L, i)
        max_index = find_max_index(L, j)
        swap(L, i, min_index)
        if max_index == i:
            max_index = min_index
        swap(L, j, max_index)
        i+=1
        j-=1


#selection_sort2 is fucked atm and I don't know why
def selection_sort23(L):
    for i in range(len(L) // 2):
        lower_bound, upper_bound = find_bounds(L, i)
        '''
        print(lower_bound, upper_bound)
        print(L)
        swap(L, len(L) - (i + 1), upper_bound)
        print(L)
        swap(L, i, lower_bound)
        print(L)
        '''


        
def find_bounds(L, n):
    min_index = n
    max_index = n
    for i in range(n+1, len(L)-n):
        if L[i] < L[min_index]:
            min_index = i
        elif L[i] > L[max_index]:
            max_index = i
    return min_index,max_index

test = create_random_list(10,10)
selection_sort2(test)