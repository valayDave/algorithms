from typing import List

def merge(part_one:List[int],part_two:List[int])->List[int]:
    larger = None
    smaller = None
    new_arr = []
    # print("Processing",part_one,part_two)
    if len(part_one) > len(part_two):
        larger = part_one
        smaller = part_two
    else:
        larger = part_two
        smaller = part_one
    s_pref = smaller.pop(0)
    l_elem = larger.pop(0)

    while True:
        if l_elem > s_pref:
            new_arr.append(s_pref)
            if len(smaller) > 0:
                s_pref = smaller.pop(0)
            else:
                new_arr+=[l_elem]
                if len(larger) > 0:
                    new_arr+=larger
                break
            # print("Adding Here Smaller",new_arr,l_elem,s_pref,larger,smaller)
        else:
            new_arr.append(l_elem)
            if len(larger) > 0:
                l_elem = larger.pop(0)
            else:
                new_arr+=[s_pref]
                if len(smaller) > 0:
                    new_arr+=smaller
                break
            
            # print("Adding Here Larger",new_arr,l_elem,s_pref,larger,smaller)
    # print("Returning ",new_arr)
    return new_arr
    

def divide_and_sort(arr:List[int]):
    length = len(arr)//2
    # print("Length : ",length)
    part_one = arr[:length]
    part_two = arr[length:]
    if length == 1:
        new_arr = []
        if len(part_one) == len(part_two):
            if part_one[0] > part_two[0]:
                new_arr =[part_two[0],part_one[0]] 
            else:
                new_arr =[part_one[0],part_two[0]] 
            return new_arr
        else:
            larger = None
            smaller = None
            if len(part_one) > len(part_two):
                larger = divide_and_sort(part_one)
                smaller = part_two
            else:
                larger = divide_and_sort(part_two)
                smaller = part_one
            return merge(larger,smaller)

    elif length > 1:
        part_one = divide_and_sort(part_one)
        # print("Part One ! ",part_one)
        part_two = divide_and_sort(part_two)
        # print("Part Two ! ",part_two)
        return merge(part_one,part_two)


# $ Algorithm runs by swapping value by comparing neighbors.  
def merge_sort(arr:List[int])->List[int]:
    if len(arr) == 0:
        return []
    return divide_and_sort(arr)

# x = [3, 4, 1, 8, 2, 5, 4, 3, 2, 3, 5, 9, 0, 2, 9, 5, 9, 4, 2, 1]
# print(merge_sort(x))
# print(sorted(x))
