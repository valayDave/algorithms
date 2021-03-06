from typing import List

test_cases = [
    ([0,1,0,2,1,0,1,3,2,1,2,1],6),
    ([4,2,3],1),
    ([2,1,0,2],3),
    ([2,2,2,2,2],0),
    ([2,3,1,1,1,1,3],8),
    ([5,4,1,2],1),
    ([5,2,1,2,1,5],14),
    ([5,5,1,7,1,1,5,2,7,6],23),
    ([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3],83),
    ([9,6,8,8,5,6,3],3),
    ([2,6,3,8,2,7,2,5,0],11),
    ([0,0,0,2,0,8,6,7,7],3)
]


# $ Conditions of the problem : 
    # $ if len(list) == 1 or 0 
        # $ return 0 
    # $ y1 > 0, y2 > 0,...yi,y{i+1} > 0 , y{i+1} > y{i} and y1 > y2 >= y3 >= .... y{i}
            # $ collect_water
    # $ y1 > 0, y2 > 0,...yi > 0 , y{i+1} = 0 and y1 > y2 >= y3 >= .... y{i}
        # $ Iterate untill y{i+k} > 0 and list is not empty:
            # $ collect_water
        # $ Else : 
            # $ dont_collect_water 
def collect_water(height:List[int],largest_lhs_column_height:int,collected_water = 0) -> int:
    # print('collecting_water',height)
    if height[len(height)-1] < height[0]:
        tallest = height[len(height)-1]
        start = len(height)-2
        stop = 0
        step = -1
    else:
        tallest = height[0]
        start = 1
        stop = len(height)-1
        step = 1 
    stop_index = 0
    for i in range(start,stop,step):
        if height[i] < tallest:
            collected_water+= tallest - height[i]
        else:
            stop_index = i
            break
    if stop_index > 0:
        if (height[stop_index] == tallest and height[stop_index-1] < tallest )or (len(height[:stop_index+1]) >= 3 and height[stop_index] < largest_lhs_column_height):
            # print("Collecting Water Againg. ",height,height[:stop_index+1],height[stop_index:],collected_water)
            return collect_water(height[:stop_index+1],largest_lhs_column_height,collected_water)

    # print('collecting_water',height,tallest,collected_water,stop_index,largest_lhs_column_height)
    return collected_water

def trap_water(height:List[int]) -> int:
    if len(height) in [0,1]:
        return 0
    coordinates = list(enumerate(height))
    trapped_units = 0
    prev_x,prev_y  = None, None
    largest_lhs_column_index,largest_lhs_column_height = None,None
    coord_index = 0
    while coord_index < len(coordinates):
        largest_lhs_column_index,largest_lhs_column_height = coordinates[coord_index]
        coord_index+=1
        if largest_lhs_column_height > 0:
            break
    collected_buffer = 0
    previously_collected_from= (None,None)
    prev_x,prev_y = largest_lhs_column_index,largest_lhs_column_height    
    while coord_index < len(coordinates):
        new_x,new_y = coordinates[coord_index]
        # print(prev_y,new_y,largest_lhs_column_height,collection_buffer,trapped_units)
        if prev_y == new_y:
            if prev_x == largest_lhs_column_index: # $ This means : [4,4]
                # $ I Should Shift the largest_lhs_column_index to new_x
                largest_lhs_column_index,largest_lhs_column_height = new_x,new_y
            if coord_index == len(height)-1:
                collection_area = height[largest_lhs_column_index:new_x+1]
                collected_buffer =  collect_water(height[largest_lhs_column_index:new_x+1],largest_lhs_column_height) #collection_buffer - (largest_lhs_column_height-new_y)*(new_x - largest_lhs_column_index)+(largest_lhs_column_height-new_y) 
                previously_collected_from = (largest_lhs_column_index,new_x)

        elif prev_y < new_y: 
            if prev_x == largest_lhs_column_index: # $ This means : [3,4]
                # $ I Should Shift the largest_lhs_column_index to new_x
                collection_buffer = 0                    
                largest_lhs_column_index,largest_lhs_column_height = new_x,new_y
                pass
            elif prev_y < largest_lhs_column_height: # $ This means : [6,3,4] or [4,3,4] or [3,2,4]
                if new_y < largest_lhs_column_height: # $ This means : [6,3,4]
                    if coord_index == len(height)-1:
                        collection_area = height[largest_lhs_column_index:new_x+1]
                        collected_buffer =  collect_water(height[largest_lhs_column_index:new_x+1],largest_lhs_column_height) #collection_buffer - (largest_lhs_column_height-new_y)*(new_x - largest_lhs_column_index)+(largest_lhs_column_height-new_y) 
                        previously_collected_from = (largest_lhs_column_index,new_x)
                        # largest_lhs_column_index,largest_lhs_column_height = new_x,new_y
                else:# $ This means : [3,2,3] or [3,2,4] : If new_y >= largest_lhs_column_height new_y can be used for calc of buffer. 
                    collection_area = height[largest_lhs_column_index:new_x+1]
                    collected_buffer =  collect_water(collection_area,largest_lhs_column_height) #collection_buffer - (largest_lhs_column_height-new_y)*(new_x - largest_lhs_column_index)+(largest_lhs_column_height-new_y) 
                    trapped_units+=collected_buffer
                    collected_buffer = 0
                    previously_collected_from = (largest_lhs_column_index,new_x)
                    largest_lhs_column_index,largest_lhs_column_height = new_x,new_y
        else:
            if coord_index == len(height)-1:
                collection_area = height[largest_lhs_column_index:new_x+1]
                collected_buffer =  collect_water(height[largest_lhs_column_index:new_x+1],largest_lhs_column_height) #collection_buffer - (largest_lhs_column_height-new_y)*(new_x - largest_lhs_column_index)+(largest_lhs_column_height-new_y) 
                previously_collected_from = (largest_lhs_column_index,new_x)
        prev_x,prev_y = new_x,new_y  
        coord_index+=1
    # print("trapped Water : ",trapped_units,collected_buffer)
    trapped_units+=collected_buffer
    return trapped_units

        
for test_case,expected_op in test_cases:
    op = trap_water(test_case)
    print(test_case,op,expected_op,op == expected_op)
