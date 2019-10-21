from typing import List
import numpy as np

# $ pos is always from right and pos >=1
def get_digit(num:int,pos:int):
    remainder,n = None,num
    while pos > 0:
        n,remainder = divmod(n,10)
        pos-=1
    return remainder

# $ Does the counting sort by digits. 
def counting_sort_by_digit(arr:List[int],pos:int):
    count_map =[[] for i in range(0,10)]
    for i in arr: # Will have to ensure that arr[i] < 9
        remainder = get_digit(i,pos)
        count_map[remainder].append(i)
    new_arr = []
    
    for i in range(0,count_map.__len__()):
        while count_map[i].__len__() > 0:
           new_arr.append(count_map[i].pop(0))
    
    return new_arr

def radix_sort(arr:List[int]):
    max_value = max(arr)
    digit_counter = 1
    while max_value > 0:
        arr = counting_sort_by_digit(arr,digit_counter)
        digit_counter+=1
        max_value= max_value//10
    
    return arr


# x = np.random.randint(30,size=10)
# print(list(x))
# print(radix_sort(list(x)))