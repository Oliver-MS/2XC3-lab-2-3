from bad_sorts import selection_sort, bubble_sort, selection_sort2, bubble_sort2, create_random_list
import time
import matplotlib.pyplot as plt

#Each of the three bad sorts will be tested on identical randomly generated lists of increasing size.
#The average time it takes to sort a list will be graphed.

experiments = 750
max_list_size = 100
max_val = 100

bubble_times = []
selection_times = []
bubble2_times = []
selection2_times = []
insertion_times = []
sizes = []
for i in range(max_list_size):
    total_bubble_time = 0
    total_selection_time = 0
    total_bubble2_time = 0
    total_selection2_time = 0
    for _ in range(experiments):
        rand_list1 = create_random_list(i,max_val)
        rand_list2 = rand_list1.copy()
        rand_list3 = rand_list1.copy()
        rand_list4 = rand_list1.copy()
        
        #before = time.perf_counter() 
        #bubble_sort(rand_list1)
        #after = time.perf_counter()
        #total_bubble_time += (after - before)
        
        before = time.perf_counter() 
        selection_sort(rand_list2)
        after = time.perf_counter()
        total_selection_time += (after - before)

        #before = time.perf_counter() 
        #bubble_sort2(rand_list3)
        #after = time.perf_counter()
        #total_bubble2_time += (after - before)
        
        before = time.perf_counter() 
        selection_sort2(rand_list4)
        after = time.perf_counter()
        total_selection2_time += (after - before)
        
        
    sizes.append(i)
    #bubble_times.append(total_bubble_time / experiments)
    selection_times.append(total_selection_time / experiments)
    #bubble2_times.append(total_bubble2_time / experiments)
    selection2_times.append(total_selection2_time / experiments)
    
#plt.plot(sizes, bubble_times, label="bubble_sort")
plt.plot(sizes, selection_times, label="selection_sort")
#plt.plot(sizes, bubble2_times, label="bubble_sort2")
plt.plot(sizes, selection2_times, label="selection_sort2")

plt.xlabel("size of list")
plt.ylabel("time to sort (seconds)")
plt.title(f"Comparing the Runtime of Selection Sort and Optimized Selection Sort\nAveraged Over {experiments} Experiments")
plt.legend()
plt.show()

