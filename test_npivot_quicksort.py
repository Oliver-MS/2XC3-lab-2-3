from good_sorts import npivot_quicksort
from bad_sorts import create_random_list

import time
from matplotlib import pyplot as plt
    
#testing
experiments = 50
max_list_size = 300
max_val = 500
max_pivots = 50
pivot_step = 5

n_quicksort_times = []
total_times = []
sizes = []
for p in range(1,max_pivots+1,pivot_step):
    n_quicksort_times.append([])
    total_times.append(0)

for i in range(max_list_size):
    for p in range(len(total_times)):
        total_times[p] = 0
    for _ in range(experiments):
        rand_list = create_random_list(i,max_val)
        for p in range(len(total_times)):
            subject = rand_list.copy()
            
            before = time.perf_counter() 
            npivot_quicksort(subject,(p+1)*pivot_step)
            after = time.perf_counter()
            total_times[p] += (after - before)
            
    sizes.append(i)
    for p in range(len(n_quicksort_times)):
        n_quicksort_times[p].append(total_times[p] / experiments)
    
for p in range(len(n_quicksort_times)):
    plt.plot(sizes, n_quicksort_times[p], label=f"{(p+1)*pivot_step} pivot(s)")

plt.xlabel("size of list")
plt.ylabel("time to sort (seconds)")
plt.title(f"Comparing the Runtime of Quicksort Implementations with\nDifferent Numbers of Pivots, Averaged Over {experiments} Experiments")
plt.legend()
plt.show()
