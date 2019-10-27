from typing import List



def create_node(i,j,node_graph):
    map_index = str(i)+str(j)
    if map_index not in node_graph:
        node_graph[map_index] = set()
    return map_index


def maximal_rectangle(matrix: List[List[str]]):
    rect_rows = None
    rect_cols = None
    node_graph = {}
    one_indexes = []
    for i in range(len(matrix)):
        row = matrix[i]
        one_arr = []
        start_index = None
        for j in range(len(row)):
            if row[j] != '1':
                if start_index is not None:
                    one_arr.append((start_index,j-1))
                    start_index = None
            else:
                if start_index is None:
                    start_index = j
        if start_index is not None:
            one_arr.append((start_index,len(row)-1))
        one_indexes.append(one_arr)
    max_counter = 0
    # print(one_indexes)
    for i in range(len(one_indexes)):
        row_index_tuple_arr = one_indexes[i]
        for start_index,end_index in row_index_tuple_arr:
            current_units_counter = (end_index+1)-start_index
            current_units = current_units_counter 
            # print("Setting Current Units Of ",current_units,start_index,end_index)
            j_start = i-1 if i > 0 else i+1  
            for j in range(j_start,len(one_indexes)):
                found_match = False
                if j == i:
                    continue
                next_row_index_tuple_arr = one_indexes[j]
                for next_start_index,next_end_index in next_row_index_tuple_arr:
                    # print((start_index,end_index),i,'      ',(next_start_index,next_end_index),current_units,j)
                    if (start_index == next_start_index and end_index == start_index):
                        current_units += current_units_counter
                        found_match = True
                    elif ((start_index <= next_end_index) and next_start_index <= start_index and (next_end_index+1 - next_start_index)>=current_units_counter) and next_end_index >=end_index and start_index!=end_index:
                        current_units += current_units_counter
                        found_match = True
                         
                
                if not found_match and j > i:
                    break
                    # else:
                    #     break
            if current_units > max_counter:
                # print("setting Counter :::: ",current_units,i)
                max_counter = current_units
    return max_counter

k1 = [
    ["0","0","0","1","0","1","1","1"],
    ["0","1","1","0","0","1","0","1"],
    ["1","0","1","1","1","1","0","1"],
    ["0","0","0","1","0","0","0","0"],
    ["0","0","1","0","0","0","1","0"],
    ["1","1","1","0","0","1","1","1"],
    ["1","0","0","1","1","0","0","1"],
    ["0","1","0","0","1","1","0","0"],
    ["1","0","0","1","0","0","0","0"]
] # 4


x = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
] # 6


y = [
  ["1","1","1","0"],
  ["1","1","1","1"],
  ["1","1","1","1"],
  ["1","0","0","1"]
] # 9

z = [
  ["1","1","0","0","0"],
  ["1","1","0","1","1"],
  ["1","1","0","1","1"],
  ["1","1","0","1","1"]
] # 8
t = [
    ["1","0","1","0"],
    ["1","0","1","1"],
    ["1","0","1","1"],
    ["1","1","1","1"]
] # 6 

k = [
    ["1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","0","0","0"],
    ["0","1","1","1","1","0","0","0"]
] # 21
q = [
    ["0","1","1","0","1"],
    ["1","1","0","1","0"],
    ["0","1","1","1","0"],
    ["1","1","1","1","0"],
    ["1","1","1","1","1"],
    ["0","0","0","0","0"]
] # 9

q1 = [
    ["1","0","1","0"],
    ["1","0","1","1"],
    ["1","0","1","1"],
    ["1","1","1","1"]
] #6

print(maximal_rectangle(x),'x')
print(maximal_rectangle(y),'y')
print(maximal_rectangle(t),'t')
print(maximal_rectangle(z),'z')
print(maximal_rectangle(q1),'q1')
print(maximal_rectangle(k1),'k1')
print(maximal_rectangle(q),'q')
print(maximal_rectangle(k),'k')