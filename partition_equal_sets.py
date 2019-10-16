'''
    Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

    Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.


    Example 1:

    Input: [1, 5, 11, 5]

    Output: true

    Explanation: The array can be partitioned as [1, 5, 5] and [11].


    Example 2:

    Input: [1, 2, 3, 5]

    Output: false

    Explanation: The array cannot be partitioned into equal sum subsets.

'''
from typing import List

def optimise(a1:List[int],a2:List[int],num):
    # This is called when both arrays togather are smaller than num so transfer data from one to other and return them back
    a1 += a2
    a2 = [num]
    return a1,a2

# Minimization happens when arrays are nearly same size or one with larger sum is of smaller length than one with biggest sum. 
def minimize(larger_sum_arr,smaller_sum_arr,some_num):
    found_result = False
    # print("Minimising Elements",some_num,sum(larger_sum_arr),sum(smaller_sum_arr),len(larger_sum_arr),len(smaller_sum_arr),smaller_sum_arr[len(smaller_sum_arr)-1],smaller_sum_arr[0])
    if len(larger_sum_arr) <= len(smaller_sum_arr):
        larger_sum_arr.sort()
        smaller_sum_arr.sort(reverse=True)
        if smaller_sum_arr[len(smaller_sum_arr)-1] < some_num or smaller_sum_arr[0] > some_num: # $  the difference is bigger than Smallest Elem in larger.
            for index_s,curr_s in enumerate(smaller_sum_arr):
                for index_l,curr_l in enumerate(larger_sum_arr):
                    # print("Checking :: ",curr_l,curr_s,2*(curr_l - curr_s),some_num,2*(curr_l - curr_s) == some_num)
                    if 2*(curr_l - curr_s) == some_num: # .
                        larger_sum_arr[index_l] = curr_s
                        smaller_sum_arr[index_s] = curr_l
                        found_result = True
                        break
                if found_result:
                    break
    else:
        larger_sum_arr.sort()
        smaller_sum_arr.sort(reverse=True)
        if smaller_sum_arr[0] > some_num:
            for index_s,curr_s in enumerate(smaller_sum_arr):
                for index_l,curr_l in enumerate(larger_sum_arr):
                    if 2*(curr_l - curr_s) == some_num:
                        larger_sum_arr[index_l] = curr_s
                        smaller_sum_arr[index_s] = curr_l
                        found_result = True
                        break
                if found_result:
                    break

    return larger_sum_arr,smaller_sum_arr,found_result

# This method will shift until the best result or an array with a larger sum is smaller in length than an array with smaller sum. 
def shift_elements(larger_sum_arr:List[int],smaller_sum_arr:List[int],shift_counter:int):
    larger_sum_arr.sort()
    if larger_sum_arr[0]+sum(smaller_sum_arr) < sum(larger_sum_arr) :
        shifting_number = larger_sum_arr.pop(0)
        smaller_sum_arr+=[shifting_number]
        shift_counter+=1
        return shift_elements(larger_sum_arr,smaller_sum_arr,shift_counter)
    else:
        return larger_sum_arr,smaller_sum_arr,shift_counter


def distribute(a1:List[int],a2:List[int],num):
    # This will distribute this number among the arrays.
    larger = None
    smaller = None
    a1_sum = sum(a1)
    a2_sum = sum(a2)
    if a1_sum > a2_sum:
        larger = a1
        smaller = a2
    else:
        larger = a2
        smaller = a1
    smaller = smaller+[num]
    larger_sum = sum(larger)
    smaller_sum = sum(smaller)
    new_sum_difference  = smaller_sum - larger_sum
    larger_sum_arr = smaller
    smaller_sum_arr = larger
    if new_sum_difference < 0:
        larger_sum_arr = larger
        smaller_sum_arr = smaller
    
    some_num  = sum(larger_sum_arr) - sum(smaller_sum_arr)

    if len(larger_sum_arr) > len(smaller_sum_arr):
        shift_counter = 0
        larger_sum_arr,smaller_sum_arr,shift_counter = shift_elements(larger_sum_arr,smaller_sum_arr,shift_counter)
        # print("Shifted Elements", shift_counter,some_num)#larger_sum_arr,smaller_sum_arr,)
    
    some_num  = sum(larger_sum_arr) - sum(smaller_sum_arr)
    if some_num < 0:
        larger_sum_arr,smaller_sum_arr = smaller_sum_arr,larger_sum_arr
        some_num = sum(larger_sum_arr) - sum(smaller_sum_arr)
    #     print("Value Of some_num After change ::: ",some_num)
    # print("Value Of some_num From Here ::: ",some_num)
    
    prev_value = some_num
    change_shift = True
    # print("Starting Minimizing Loop ~! ",some_num,num)
    while some_num % 2 == 0 and change_shift and some_num!=0:
        # if some_num > 0:
        larger_sum_arr,smaller_sum_arr,change_shift = minimize(larger_sum_arr,smaller_sum_arr,some_num)
        some_num  = sum(larger_sum_arr) - sum(smaller_sum_arr)
        # print("Value Of some_num From Here ::: ",some_num,len(larger_sum_arr),len(smaller_sum_arr),change_shift)
    
    return larger_sum_arr,smaller_sum_arr

def partion_equal_sets(nums:List[int]):
    if nums.__len__() == 1:
        return False
    # nums.sort()
    arr_sum = sum(nums)
    a1 = []
    a2 = []
    for i in range(0,nums.__len__()):
        if a1.__len__() == 0 and a2.__len__() == 0:
            a1.append(nums[i])
            continue
        if nums[i] >= sum(a1) + sum(a2):
            a1,a2 = optimise(a1,a2,nums[i])
        else:
            a1,a2 = distribute(a1,a2,nums[i])
        # print(a1,a2,sum(a1) - sum(a2))
    return sum(a1) == sum(a2)


test_cases = [
    ([1, 2, 3, 5],False),
    ([1, 5, 11, 5],True),
    ([1, 1, 1, 1],True),
    ([1,3,4,6,2,5,7],True),
    ([1,6,5,3,2,4,7],True),
    ([1,1,2,5,5,5,5],True),
    ([1, 2, 3, 4,5,5,3],False),
    ([3,3,3,4,5],True),
    ([1],False),
    ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,90],True),
    ([66,90,7,6,32,16,2,78,69,88,85,26,3,9,58,65,30,96,11,31,99,49,63,83,79,97,20,64,81,80,25,69,9,75,23,70,26,71,25,54,1,40,41,82,32,10,26,33,50,71,5,91,59,96,9,15,46,70,26,32,49,35,80,21,34,95,51,66,17,71,28,88,46,21,31,71,42,2,98,96,40,65,92,43,68,14,98,38,13,77,14,13,60,79,52,46,9,13,25,8],True)
    ]
for test_case,expected_op in test_cases:
    op = partion_equal_sets(test_case)
    print(test_case,expected_op,op,expected_op == op,'\n\n')