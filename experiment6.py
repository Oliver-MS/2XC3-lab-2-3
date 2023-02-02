from bad_sorts import create_random_list
import time
from matplotlib import pyplot as plt

#original quicksort definition
def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

#modified quicksort definition
def quicksort2(L):
    copy = quicksort_copy2(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy2(L):
    if len(L) < 2:
        return L
    pivot1 = L[0]
    pivot2 = L[1]
    left, middle, right = [], [], []
    for num in L[2:]:
        if num < pivot1 and num < pivot2:
            left.append(num)
        elif (num >= pivot1 and num < pivot2) or (num >= pivot2 and num < pivot1):
            middle.append(num)
        else:
            right.append(num)
    if pivot1 < pivot2:
        return quicksort_copy2(left) + [pivot1] + quicksort_copy2(middle) + [pivot2] + quicksort_copy2(right)
    else:
        return quicksort_copy2(left) + [pivot2] + quicksort_copy2(middle) + [pivot1] + quicksort_copy2(right)
    
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