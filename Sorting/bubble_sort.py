# import testcases as test_case_holder
from typing import List

# $ Algorithm runs by swapping value by comparing neighbors.  
def bubble_sort(arr:List[int])->List[int]:
    while True:
        value_changed = False
        for j in range(0,arr.__len__()-1):
            if arr[j] > arr[j+1]:
                value_changed = True
                # Swapping values when greater. 
                arr[j],arr[j+1] = arr[j+1],arr[j]
        
        if value_changed:
            prev_swap = arr        
        else:
            break
    return arr

# no_case_failed = True
# for test_case,expected_op in test_case_holder.test_cases:
#     op = list(bubble_sort(test_case))
#     if op == expected_op:
#         continue
#     else:
#         print("Test Case Fail : ",test_case,op,expected_op,op == expected_op)
#         no_case_failed = False

# if no_case_failed:
#     print("All Tests Passed :) ")