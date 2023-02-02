from bad_sorts import selection_sort, bubble_sort, insertion_sort, create_random_list
import time
import matplotlib.pyplot as plt

#Each of the three bad sorts will be tested on identical randomly generated lists of increasing size.
#The average time it takes to sort a list will be graphed.

experiments = 750
max_list_size = 100
max_val = 100

bubble_times = []
selection_times = []
insertion_times = []
sizes = []
for i in range(max_list_size):
    total_bubble_time = 0
    total_selection_time = 0
    total_insertion_time = 0
    for _ in range(experiments):
        rand_list1 = create_random_list(i,max_val)
        rand_list2 = rand_list1.copy()
        rand_list3 = rand_list1.copy()
        
        before = time.perf_counter() 
        bubble_sort(rand_list1)
        after = time.perf_counter()
        total_bubble_time += (after - before)
        
        before = time.perf_counter() 
        selection_sort(rand_list2)
        after = time.perf_counter()
        total_selection_time += (after - before)
        
        before = time.perf_counter() 
        insertion_sort(rand_list3)
        after = time.perf_counter()
        total_insertion_time += (after - before)
        
    sizes.append(i)
    bubble_times.append(total_bubble_time / experiments)
    selection_times.append(total_selection_time / experiments)
    insertion_times.append(total_insertion_time / experiments)
    
plt.plot(sizes, bubble_times, label="bubble_sort")
plt.plot(sizes, selection_times, label="selection_sort")
plt.plot(sizes, insertion_times, label="insertion_sort")

plt.xlabel("size of list")
plt.ylabel("time to sort (seconds)")
plt.title(f"Comparing the Runtime of Bubble Sort, Selection Sort, and Insertion Sort,\nAveraged Over {experiments} Experiments")
plt.legend()
plt.show()