import numpy as np
from bubble_sort import bubble_sort
from heap_sort import heap_sort
from heap_sort import heapSort_GFG
from radix_sort import radix_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

test_cases = [
    
]
import random
for i in range(0,30):
    # y = np.random.randint(120000,size = random.randint(1,300))
    # y = np.random.randint(100000,size = 20000)
    y = np.random.randint(100,size = 2000)
    x = list(y)
    x.sort()
    test_cases.append((y,x))

algos_to_test = [
    # (heapSort_GFG,'heapSort_GFG'),
    # (heap_sort,'heap_sort'),
    (bubble_sort,'bubble_sort'),
    (radix_sort,'radix_sort'),
    (insertion_sort,'insertion_sort'),
    (merge_sort,'merge_sort')
]

for algo,algo_name in algos_to_test:
    no_case_failed = True
    failed_count =  0
    num_completed = 0
    for test_case,expected_op in test_cases:
        # print("Checking : ",test_case)
        op = list(algo(list(test_case)))
        if op == expected_op:
            continue
        else:
            failed_count+=1
            print("Test Case Failed For "+algo_name+' : ',list(test_case),op,expected_op,op == expected_op,'\n')
            no_case_failed = False

    if no_case_failed:
        print("All Tests Passed For "+  algo_name +" :) ",len(test_cases))
    else:
        print("Num Tests Passed For "+  algo_name +" : ",len(test_cases)-failed_count," From ",len(test_cases))