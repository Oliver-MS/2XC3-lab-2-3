from bad_sorts import create_random_list
from good_sorts import quicksort, quicksort2, npivot_quicksort
import time
from matplotlib import pyplot as plt
    
#testing
experiments = 1000
max_list_size = 150
max_val = 100

quicksort_times = []
quicksort2_times = []
sizes = []

for i in range(max_list_size):
    quicksort_total_time = 0
    quicksort2_total_time = 0
    for _ in range(experiments):
        rand_list1 = create_random_list(i,max_val)
        rand_list2 = rand_list1.copy()
        
        before = time.perf_counter() 
        quicksort(rand_list1)
        after = time.perf_counter()
        quicksort_total_time += (after - before)
        
        before = time.perf_counter() 
        quicksort2(rand_list2)
        after = time.perf_counter()
        quicksort2_total_time += (after - before)
        
    sizes.append(i)
    quicksort_times.append(quicksort_total_time / experiments)
    quicksort2_times.append(quicksort2_total_time / experiments)
    
plt.plot(sizes, quicksort_times, label="quicksort")
plt.plot(sizes, quicksort2_times, label="modified quicksort")

plt.xlabel("size of list")
plt.ylabel("time to sort (seconds)")
plt.title(f"Comparing the Runtime of a Given Quicksort Implementation with\na Modified Implementation, Averaged Over {experiments} Experiments")
plt.legend()
plt.show()