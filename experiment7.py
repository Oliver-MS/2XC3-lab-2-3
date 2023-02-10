import time

import matplotlib.pyplot as plt

from bad_sorts import create_random_list
from good_sorts import mergesort, merge

experiments = 750
max_list_size = 100
max_val = 100

merge_times = []
bottom_up_merge_times = []
sizes = []

# new mergesort function that uses bottom-up mergesort
def bottom_up_mergesort(L):
    width = 1
    n = len(L)
    while (width < n):
        left_ind = 0
        while (left_ind < n):
            # this is the index of the last element in the right sublist
            right_ind = min(left_ind + 2 * width - 1, n - 1)
            # this is the index of the last element in the left sublist
            middle_ind = min(left_ind + width - 1, n - 1)

            bottom_up_merge(L, left_ind, middle_ind, right_ind)
            # this moves the left index to the start of the next pair of sublists
            left_ind += 2 * width
        width *= 2
    return L

# we define a new merge function because the one in good_sorts.py is not in-place
def bottom_up_merge(L, left_ind, middle_ind, right_ind):
    # this splits the list into two sublists
    left = L[left_ind:middle_ind+1]
    right = L[middle_ind+1:right_ind+1]
    i = j = 0
    k = left_ind
    
    # this replaces the elements in L with the elements in the sublists depending on which is smaller
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            L[k] = left[i]
            i += 1
        else:
            L[k] = right[j]
            j += 1
        k += 1
    
    # this adds elements from the left sublist if there are any left
    while i < len(left):
        L[k] = left[i]
        i += 1
        k += 1
    
    # this adds elements from the right sublist if there are any left
    while j < len(right):
        L[k] = right[j]
        j += 1
        k += 1

for i in range(max_list_size):
    total_bottom_up_merge_time = 0
    total_merge_time = 0
    for _ in range(experiments):
        rand_list1 = create_random_list(i, max_val)
        rand_list2 = rand_list1.copy()
        
        #bottom_up_mergesort
        before = time.perf_counter() 
        bottom_up_mergesort(rand_list1)
        after = time.perf_counter()
        total_bottom_up_merge_time += (after - before)
        
        #mergesort
        before = time.perf_counter() 
        mergesort(rand_list2)
        after = time.perf_counter()
        total_merge_time += (after - before)
        
    sizes.append(i)
    bottom_up_merge_times.append(total_bottom_up_merge_time / experiments)
    merge_times.append(total_merge_time / experiments)

plt.plot(sizes, bottom_up_merge_times, label = "bottom up mergesort")
plt.plot(sizes, merge_times, label = "mergesort")

plt.xlabel("size of list")
plt.ylabel("time to sort (seconds)")
plt.title(f"Comparing the Runtime of Bottom Up Mergesort and Traditional Mergesort\nwith Lists of Size {max_list_size}, Averaged Over {experiments} Experiments")
plt.legend()
plt.show()