import math
import time

from matplotlib import pyplot as plt

from bad_sorts import create_random_list, insertion_sort
from good_sorts import mergesort, quicksort

experiments = 1000
list_size = 9
max_val = 9

quick_times = []
insertion_times = []
merge_times = []
sizes = []
for i in range(list_size):
    total_quick_time = 0
    total_insertion_time = 0
    total_merge_time = 0
    for _ in range(experiments):
        rand_list1 = create_random_list(i, max_val)
        rand_list2 = rand_list1.copy()
        rand_list3 = rand_list1.copy()
        
        #quicksort
        before = time.perf_counter() 
        quicksort(rand_list1)
        after = time.perf_counter()
        total_quick_time += (after - before)
        
        #insertionsort
        before = time.perf_counter() 
        insertion_sort(rand_list2)
        after = time.perf_counter()
        total_insertion_time += (after - before)
        
        #mergesort
        before = time.perf_counter() 
        mergesort(rand_list3)
        after = time.perf_counter()
        total_merge_time += (after - before)
        
    sizes.append(i)
    quick_times.append(total_quick_time / experiments)
    insertion_times.append(total_insertion_time / experiments)
    merge_times.append(total_merge_time / experiments)
        
plt.plot(sizes, quick_times, label="quicksort")
plt.plot(sizes, insertion_times, label="insertionsort")
plt.plot(sizes, merge_times, label="mergesort")

plt.xlabel("size of list")
plt.ylabel("time to sort (seconds)")
plt.title(f"Comparing the Runtime of Quicksort, Insertionsort, and Mergesort\nwith Lists of Size {list_size}, Averaged Over {experiments} Experiments")
plt.legend()
plt.show()