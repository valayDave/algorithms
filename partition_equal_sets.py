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
    some_num  = smaller_sum - larger_sum
    if some_num > 0:
        found_result = False
        smaller.sort()
        larger.sort(reverse=True)
        # print("Doing It ",larger[len(larger)-1],some_num)
        # # $ Move Items from smaller into larger to minimise difference
        if larger[len(larger)-1] < some_num: # $  the difference is bigger than Smallest Elem in larger.  
            for index_l,curr_l in enumerate(larger):
            # while itr1.__length_hint__() > 0:
                for index_s,curr_s in enumerate(smaller):
                    if 2*(curr_s - curr_l) == some_num: # . 
                        smaller[index_s] = curr_l
                        larger[index_l] = curr_s
                        found_result = True
                        break
                if found_result:
                    break
                    # print("Found Something. ")
    return larger,smaller
   
    

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
        # elif a2.__len__() == 0:
        #     a2.append(nums[i])
        #     continue
        
        if nums[i] >= sum(a1) + sum(a2):
            a1,a2 = optimise(a1,a2,nums[i])
        else:
            a1,a2 = distribute(a1,a2,nums[i])
        print(a1,a2,sum(a1) - sum(a2)) 
        
    return sum(a1) == sum(a2)


test_cases = [
    ([1, 2, 3, 5],False),
    ([1, 5, 11, 5],True),
    ([1, 1, 1, 1],True),
    ([1,3,4,6,2,5,7],True),
    ([1,6,5,3,2,4,7],True),
    ([1,1,2,5,5,5,5],True),
    # ([1, 2, 3, 4,5,5,3],True),
    ([1],False),
    ]
for test_case,expected_op in test_cases:
    op = partion_equal_sets(test_case)
    print(test_case,expected_op,op,expected_op == op)