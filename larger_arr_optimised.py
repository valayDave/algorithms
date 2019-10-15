from typing import List
import functools

test_cases = [
    #(A,K,op)
    ([1, 4, 3, 2, 5],4,[4,3,2,5]),
    ([1,2,3,1,2,3,1,2,5],2,[3,1]),
    ([1, 2, 4, 3, 5],3,[4, 3, 5]),
    ([1],1,[1]),
    ([1,2,1,2,12],1,[12]),
    ([1,2,1,2,12],2,[2,12]),
    ([11,1,1,1],2,[11,1]),
    ([1, 4, 3, 2, 5],2,[4,3]),
    ([10, 2, 33, 2, 4,55,6],2,[55,6])
]

def generate_sub_arrs(main_arr:List[int],K):
    sub_arrs = [main_arr[i:i+K] for i in range((main_arr.__len__() - K)+1)]
    return sub_arrs

# Returns 0 , 1 , -1 or equals
def larger_sub_arr(arr1:List[int],arr2:List[int]):
    diff_arr =[arr1[i]-arr2[i] for i in range(arr1.__len__())]
    for diff in diff_arr:
        if diff == 0 : 
            continue
        elif diff > 0:
            return 1
        else:
            return -1
    return 0
        
def largest_contig_subarr(main_arr,K):       
    sub_arrs = generate_sub_arrs(main_arr,K)
    if len(sub_arrs) == 1:
        return main_arr
    largest_arr = None
    for i in range(sub_arrs.__len__()):
        if i==0:
            largest_arr = sub_arrs[i]
            continue
        largness_op = larger_sub_arr(largest_arr,sub_arrs[i])
        if largness_op == -1:
            largest_arr = sub_arrs[i]
    
    return largest_arr


def largest_contig_subarr_optimised(main_arr:List[int],K:int):
    if K == 1 : 
        return [max(main_arr)]
    largest_index = 0
    largest_arr = None
    for i in range((main_arr.__len__() - K)+1):
        if (main_arr[largest_index] - main_arr[i]) < 0:
            largest_index = i
    largest_arr = main_arr[largest_index:largest_index+K]
    return largest_arr 

def findSubarray(a, k, n): 
    # Data-structure to store all 
    # the sub-arrays of size K 
    vec=[] 
  
    # Iterate to find all the sub-arrays 
    for i in range(n-k+1): 
        temp=[] 
  
        # Store the sub-array elements in the array 
        for j in range(i,i+k): 
            temp.append(a[j]) 
  
        # Push the vector in the container 
        vec.append(temp) 
  
    # Sort the vector of elements 
    vec=sorted(vec) 
  
    # The last sub-array in the sorted order 
    # will be the answer 
    return vec[len(vec) - 1] 
  
for A,K,expected_op in test_cases:
    op = largest_contig_subarr(A,K)
    # print('ORIGINAL : ',A,K,op,expected_op,op == expected_op)
    # print('ORIGINAL : ',A,K,op,expected_op,op == expected_op)
    op2 = largest_contig_subarr(A,K)
    # print('OPTIMISED : ',A,K,op,expected_op,op2 == expected_op)
    op3 = findSubarray(A,K,len(A))
    print('CORRECT : ',A,K,op3,op==op3,op2==op3)
