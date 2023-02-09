import time

import matplotlib.pyplot as plt

from bad_sorts import create_random_list
from good_sorts import mergesort

experiments = 750
max_list_size = 100
max_val = 100

merge_times = []
bottom_up_merge_times = []
sizes = []

def bottom_up_mergesort(L):
    width = 1
    n = len(L)

    while (width < n):
        l = 0
        while (l < n):
            r = min(l + 2 * width - 1, n - 1)
            m = min(l + width - 1, n - 1)
            bottom_up_merge(L, l, m, r)
            l += 2 * width
        width *= 2
    return L

def bottom_up_merge(L, l, m, r):
    left = L[l:m+1]
    right = L[m+1:r+1]
    i = j = 0
    k = l
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            L[k] = left[i]
            i += 1
        else:
            L[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        L[k] = left[i]
        i += 1
        k += 1
    
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
plt.title(f"Comparting the Runtime of Bottom Up Mergesort and Traditional Mergesort\nwith Lists of Size {max_list_size}, Averaged Over {experiments} Experiments")
plt.legend()
plt.show()