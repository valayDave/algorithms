# import testcases as test_case_holder
from typing import List
import random

class Node:
    def __init__(self,value,id_val):
        self.left = None
        self.right = None
        self.value = value
        self.id = id_val
    
    def print(self):
        print("Current Value for Node Id "+ self.id+" : ",self.value)

def print_tree(start_node:Node):
    node_queue = []
    parent_queue = [start_node]
    print(start_node.value)
    printing_vals = [[start_node.value]]
    while True:
        current_node = parent_queue.pop(0)
        # print("Parent : ",current_node.value)
        if current_node.left is not None:
            node_queue.append(current_node.left)
            # print("Child : ",current_node.left.value)
        if current_node.right is not None:
            node_queue.append(current_node.right)
            # print("Child : ",current_node.right.value)
        if parent_queue.__len__() == 0:
            if node_queue.__len__() > 0:
                parent_queue = node_queue
                printing_vals.append(list(map(lambda a:(a.value),node_queue)))
                print(' '.join(list(map(lambda a:str(a.value),node_queue))))
                node_queue = []
            else:
                break

def create_node(value:int)->Node:    
    x = Node(value,random.randint(0,100000))
    return x

# $ Swapps the values of the nodes up to root, until parent_value > child_value
def swap_to_root(start_node:Node,minimizer=False):
    parent_queue = [start_node]
    node_queue = []
    value_flipping = False
    while True:
        current_node = parent_queue.pop(0)
        # $ Check if current_node's children are smaller/greater than parent. If they are then swap. with parent. 
        if current_node.left is not None:
            # print("Comparing : ",current_node.value," With ",current_node.left.value)
            if minimizer:
                if current_node.left.value < current_node.value:
                    current_node.left.value,current_node.value = current_node.value, current_node.left.value
                    value_flipping =True
            else:
                if current_node.left.value > current_node.value:
                    current_node.left.value,current_node.value = current_node.value, current_node.left.value     
                    value_flipping =True
            node_queue.append(current_node.left)

        if current_node.right is not None:
            # print("Comparing : ",current_node.value," With ",current_node.right.value)
            if minimizer:
                if current_node.right.value < current_node.value:
                    current_node.right.value,current_node.value = current_node.value, current_node.right.value
                    value_flipping =True
            else:
                if current_node.right.value > current_node.value:
                    current_node.right.value,current_node.value = current_node.value, current_node.right.value
                    value_flipping =True
            node_queue.append(current_node.right)

        if parent_queue.__len__() == 0:
            if node_queue.__len__() > 0:
                parent_queue = node_queue
                node_queue = []
            else:
                break

    if value_flipping:
        return swap_to_root(start_node, minimizer)
    else:
        return start_node


def create_heap(arr:List[int],minimizer=False):
    heap_root_start = create_node(arr.pop(0))
    heap_root = heap_root_start
    # $ A binary heap is a complete binary tree
    # $ all of the levels of the tree are completely filled except possibly the last level.
    # $ The nodes are filled from left to right.
    node_queue = []
    parent_queue = []
    path_to_root = [] # $ This is a stack which will hold all the nodes that will go up to root for the swapping. 
    while arr.__len__() > 0:
        curr_value = arr.pop(0)
        addition_node = create_node(curr_value)
        # print("Current Root Node : ",heap_root.id)
        if heap_root.left is None or heap_root.right is None:
            if heap_root.left is None :
                heap_root.left = addition_node
            else:
                heap_root.right = addition_node
        else:
            new_heap_root = node_queue.pop(0)
            heap_root = new_heap_root
            heap_root.left = addition_node
        
        heap_root_start = swap_to_root(heap_root_start,minimizer)
        node_queue.append(addition_node)
    
    heap_root_start = swap_to_root(heap_root_start,minimizer)

    return heap_root_start
        
def get_values_but_root(start_node:Node):
    node_queue = []
    parent_queue = [start_node]
    values = []
    while True:
        current_node = parent_queue.pop(0)
        # print("Parent : ",current_node.value)
        if current_node.left is not None:
            node_queue.append(current_node.left)
            values.append(current_node.left.value)
            # print("Child : ",current_node.left.value)
        if current_node.right is not None:
            node_queue.append(current_node.right)
            values.append(current_node.right.value)
            # print("Child : ",current_node.right.value)
        if parent_queue.__len__() == 0:
            if node_queue.__len__() > 0:
                parent_queue = node_queue
                node_queue = []
            else:
                break
    return values
    

# $ Sorts the array in Ascending
def heap_sort(arr:List[int])->List[int]: 
    current_array = arr
    sorted_array = []
    # $ repeat until the heap cant be formed. 
    while len(current_array) > 0:
        # $ Create max/min heap with elems A
        # print(current_array)
        heap_to_root = create_heap(current_array,True)
        # print("Root Element : ",heap_to_root.value)
        # $ take largest/Smallest Elem and put in arr (Root Elememt)
        sorted_array.append(heap_to_root.value)
        # $ Remove root node and from remaining values create the heap again. 
        current_array = get_values_but_root(heap_to_root)

    return sorted_array

# x = [17, 22, 12, 39, 16, 20, 15, 14, 17, 8, 9, 22, 3, 33, 39, 8, 34, 32, 14, 4, 11, 14, 20, 1, 29]
# print(heap_sort(x))