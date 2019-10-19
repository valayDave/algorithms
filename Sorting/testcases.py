import numpy as np
from bubble_sort import bubble_sort
from heap_sort import heap_sort

test_cases = [
    
]
import random
for i in range(0,30):
    y = np.random.randint(50,size = random.randint(1,40))
    x = list(y)
    x.sort()
    test_cases.append((y,x))

algos_to_test = [
    (heap_sort,'heap_sort'),
    (bubble_sort,'bubble_sort'),
]

for algo,algo_name in algos_to_test:
    no_case_failed = True
    failed_count =  0
    for test_case,expected_op in test_cases:
        op = list(algo(list(test_case)))
        if op == expected_op:
            continue
        else:
            failed_count+=1
            print("Test Case Failed For "+algo_name+' : ',list(test_case),op,expected_op,op == expected_op,'\n')
            no_case_failed = False
    if no_case_failed:
        print("All Tests Passed For "+  algo_name +" :) ")
    else:
        print("Num Tests Passed For "+  algo_name +" : ",len(test_cases)-failed_count," From ",len(test_cases))