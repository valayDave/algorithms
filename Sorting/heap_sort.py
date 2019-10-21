# import testcases as test_case_holder
from typing import List
import random

# ! This is an actual implementation. But I have done One thing wrong. 
# ! My method which swaps to the root, is inefficient and can use the rule of a heap where
# ! current.left = arr[2*i+1] and current.right = arr[2*i+2], Through this direct comparison
# ! Can be done and will save so much more time in time and space complexity. 

class Node:
    def __init__(self,value,id_val,parent_id_val):
        self.parent = parent_id_val # $ This should hold Id of parent
        self.left = None
        self.right = None
        self.value = value
        self.id = id_val
    
    def print(self):
        print("Current Value for Node Id "+ self.id+" : ",self.value)

node_map = {
    # node_id : Node
}
node_counter = 0
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

def create_node(value:int,parent_id_val:int)->Node:    
    global node_map,node_counter
    node_id = node_counter 
    x = Node(value,node_id,parent_id_val)
    node_counter+=1
    node_map[node_id] = x
    return x

# $ Swapps the values of the nodes up to root, until parent_value > child_value or parent_value < child_value based on minimizer parameter
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

def check_to_root_node(start_node:Node,minimizer=False):
    global node_map
    current_node = start_node
    # print("Start Value When Check Starts : ",start_node.value,current_node.parent)
    while current_node.parent is not None:
        if minimizer:
            if node_map[current_node.parent].value < current_node.value:
                node_map[current_node.parent].value,current_node.value = current_node.value, node_map[current_node.parent].value
                value_flipping =True
        else:
            if node_map[current_node.parent].value > current_node.value:
                node_map[current_node.parent].value,current_node.value = current_node.value, node_map[current_node.parent].value
                value_flipping =True
        current_node = node_map[current_node.parent]
    
    # print("Start Value At End : ",start_node.value)

def create_heap(arr:List[int],minimizer=False):
    heap_root_start = create_node(arr.pop(0),None)
    heap_root = heap_root_start
    # $ A binary heap is a complete binary tree
    # $ all of the levels of the tree are completely filled except possibly the last level.
    # $ The nodes are filled from left to right.
    node_queue = []
    parent_queue = []
    path_to_root = [] # $ This is a stack which will hold all the nodes that will go up to root for the swapping. 
    while arr.__len__() > 0:
        curr_value = arr.pop(0)
        addition_node = create_node(curr_value,heap_root.id)
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
        # heap_root_start = swap_to_root(heap_root_start,minimizer)
        check_to_root_node(addition_node)
        node_queue.append(addition_node)

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
    
    global node_map
    node_map.clear()
    return sorted_array

# Python program for implementation of heap Sort 
  
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
        # Heapify the root if the root is changed. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort_GFG(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        print("Calling Heapify")
        heapify(arr, n, i) 
    print(arr,'\n')

    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        print("Calling Heapify")
        heapify(arr, i, 0)
        print(arr)
    
    return arr
# x = [17, 22, 12, 39, 16, 20, 15, 14, 17, 8, 9, 22, 3, 33, 39, 8, 34, 32, 14, 4, 11, 14, 20, 1, 29]
# print(heap_sort(x))