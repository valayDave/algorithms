from typing import List

# $ Algorithm runs by swapping value by comparing neighbors.  
def insertion_sort(arr:List[int])->List[int]:
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j] < arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr