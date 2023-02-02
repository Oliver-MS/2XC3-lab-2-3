from good_sorts import quicksort, mergesort, heapsort
from bad_sorts import create_near_sorted_list
from matplotlib import pyplot as plt
import time
import math

experiments = 500
list_size = 100
max_val = 100
max_var = int(list_size * math.log(list_size) / 2)

quick_times = []
heap_times = []
merge_times = []
swaps = []
for i in range(max_var):
    total_quick_time = 0
    total_heap_time = 0
    total_merge_time = 0
    for _ in range(experiments):
        subject1 = create_near_sorted_list(list_size, max_val, i)
        subject2 = subject1.copy()
        subject3 = subject1.copy()
        
        #quicksort
        before = time.perf_counter() 
        quicksort(subject1)
        after = time.perf_counter()
        total_quick_time += (after - before)
        
        #heapsort
        before = time.perf_counter() 
        heapsort(subject2)
        after = time.perf_counter()
        total_heap_time += (after - before)
        
        #mergesort
        before = time.perf_counter() 
        mergesort(subject3)
        after = time.perf_counter()
        total_merge_time += (after - before)
        
    swaps.append(i)
    quick_times.append(total_quick_time / experiments)
    heap_times.append(total_heap_time / experiments)
    merge_times.append(total_merge_time / experiments)
        
plt.plot(swaps, quick_times, label="quicksort")
plt.plot(swaps, heap_times, label="heapsort")
plt.plot(swaps, merge_times, label="mergesort")

plt.xlabel("number of random swaps from sorted")
plt.ylabel("time to sort (seconds)")
plt.title(f"Comparing the Runtime of Quicksort, Heapsort, and Mergesort\nwith Lists of Size {list_size} with Increasing Randomness, Averaged Over {experiments} Experiments")
plt.legend()
plt.show()       