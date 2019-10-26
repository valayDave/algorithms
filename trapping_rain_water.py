from typing import List

test_cases = [
    ([0,1,0,2,1,0,1,3,2,1,2,1],6),
    ([4,2,3],1),
    ([2,1,0,2],3),
    ([2,2,2,2,2],0),
    ([2,3,1,1,1,1,3],8)
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
def trap_water(height:List[int]) -> int:
    if len(height) in [0,1]:
        return 0
    coordinates = list(enumerate(height))
    trapped_units = 0
    prev_x,prev_y  = None, None
    largest_lhs_column_index,largest_lhs_column_height = None,None
    while len(coordinates) > 0:
        largest_lhs_column_index,largest_lhs_column_height = coordinates.pop(0)
        if largest_lhs_column_height > 0:
            break
    collection_buffer = 0
    prev_x,prev_y = largest_lhs_column_index,largest_lhs_column_height    
    while len(coordinates) > 0:
        new_x,new_y = coordinates.pop(0)
        # print(prev_y,new_y,largest_lhs_column_height,collection_buffer,trapped_units)
        if prev_y > new_y:
            if prev_x == largest_lhs_column_index: # $ This means : [4,3]
                collection_buffer+=(largest_lhs_column_height-new_y)
            elif prev_y < largest_lhs_column_height: # $ [4,3,2]
                collection_buffer+=(largest_lhs_column_height-new_y)
                pass
            elif prev_y == largest_lhs_column_height: # $ This means [3,3,2]
                pass
                # ! This line Should Not Be Invoked
                print("BAD Invocation prev_y > new_y and prev_y > largest_lhs_column_height",new_y,new_x,prev_y,prev_x,largest_lhs_column_height,largest_lhs_column_index)
            elif prev_y > largest_lhs_column_height: # $ This means : [3,4,2]
                print("BAD Invocation prev_y > largest_lhs_column_height and prev_y > new_y",new_y,new_x,prev_y,prev_x,largest_lhs_column_height,largest_lhs_column_index)
                # $ Reset the value of largest_lhs and set collection_buffer = 0
                pass
            pass
        elif prev_y == new_y:
            if prev_y == 0:
                collection_buffer+=(largest_lhs_column_height)
            elif prev_x == largest_lhs_column_index: # $ This means : [4,4]
                # $ I Should Shift the largest_lhs_column_index to new_x
                largest_lhs_column_index,largest_lhs_column_height = new_x,new_y
                collection_buffer =0
                pass
            elif prev_y < largest_lhs_column_height: # $ This means : [4,3,3...]
                collection_buffer+=(largest_lhs_column_height-new_y)
                pass
            elif prev_y > largest_lhs_column_height: # $ This means : [3,4,4]
                # ! This line Should Not Be Invoked
                print("BAD Invocation prev_y == new_y and prev_y > largest_lhs_column_height",new_y,new_x,prev_y,prev_x,largest_lhs_column_height,largest_lhs_column_index)
                largest_lhs_column_index,largest_lhs_column_height = new_x,new_y
                collection_buffer =0
                pass
            pass
        else: # $ This means prev_y < new_y
            if prev_x == largest_lhs_column_index: # $ This means : [3,4]
                # $ I Should Shift the largest_lhs_column_index to new_x
                # if collection_buffer > 0:
                #     trapped_units+=collection_buffer
                collection_buffer = 0                    
                largest_lhs_column_index,largest_lhs_column_height = new_x,new_y
                pass
            elif prev_y < largest_lhs_column_height: # $ This means : [6,3,4] or [4,3,4] or [3,2,4]

                if new_y < largest_lhs_column_height: # $ This means : [6,3,4]
                    pass
                    # collection_buffer = collection_buffer - (largest_lhs_column_height-new_y)*(new_x - largest_lhs_column_index) + (new_y-prev_y)
                    if prev_y == 0:
                        collection_buffer+= (largest_lhs_column_height -new_y)
                    else:
                        collection_buffer = collection_buffer - (largest_lhs_column_height-new_y)*(new_x - largest_lhs_column_index)+(largest_lhs_column_height-new_y) 
                        trapped_units+=collection_buffer
                        collection_buffer = 0
                        largest_lhs_column_index,largest_lhs_column_height = new_x,new_y
                else:# $ This means : [3,2,3] or [3,2,4] : If new_y >= largest_lhs_column_height new_y can be used for calc of buffer. 
                    # collection_buffer+=(largest_lhs_column_height-prev_y)
                    trapped_units+=collection_buffer
                    collection_buffer = 0
                    largest_lhs_column_index,largest_lhs_column_height = new_x,new_y
                    pass
                pass
            else: # $ prev_y >= largest_lhs_column_height --> new_y >=largest_lhs_column_height
                # $ This Means : [4, 5,6]
                collection_buffer = 0
                print("BAD Invocation prev_y < new_y and prev_y > largest_lhs_column_height",new_y,new_x,prev_y,prev_x,largest_lhs_column_height,largest_lhs_column_index)
                largest_lhs_column_index,largest_lhs_column_height = new_x,new_y

        prev_x,prev_y = new_x,new_y  
    
    # print("trapped Water : ",trapped_units)
    return trapped_units

        



def trap(height:List[int])->int: 
    if len(height) in [0,1]:
        return 0
    coordinates = list(enumerate(height))
    trapped_units = 0
    largest_lhs_column_index,largest_lhs_column_height = None,None
    while len(coordinates) > 0:
        largest_lhs_column_index,largest_lhs_column_height = coordinates.pop(0)
        if largest_lhs_column_height > 0:
            break
    collection_buffer = 0
    prev_x,prev_y = largest_lhs_column_index,largest_lhs_column_height
    while len(coordinates) > 0:
        new_x,new_y = coordinates.pop(0)
        if new_y == 0:
            collection_buffer+= largest_lhs_column_height
            # print("Adding to buffer at 0 :",collection_buffer,largest_lhs_column_height)
        elif new_y <= largest_lhs_column_height:
            # print("Smaller Comp :",new_y,largest_lhs_column_height,collection_buffer)
            if prev_y > new_y and prev_x != largest_lhs_column_index:
                # print("Prev_y Greater Than new_y",new_x)
                # ! TODO : Compare for equality conditions within this. 
                collection_buffer = 0
                largest_lhs_column_index,largest_lhs_column_height  = prev_x,prev_y 
                collection_buffer+= largest_lhs_column_height - new_y
            elif prev_y < new_y:
                # ! TODO : Compare for equality conditions within this. 
                if new_y == largest_lhs_column_height or len(coordinates) == 0:
                    if len(coordinates) == 0 and new_y == largest_lhs_column_height:
                        # print('collection_buffer',collection_buffer)
                        # trapped_units+=(new_y-prev_y)+collection_buffer
                        trapped_units+=+collection_buffer
                    elif len(coordinates) == 0:
                        trapped_units+=(new_y-prev_y)
                    else:
                        trapped_units+=collection_buffer
                    collection_buffer = 0
                    largest_lhs_column_index,largest_lhs_column_height  = prev_x,prev_y
                else:
                    collection_buffer+= largest_lhs_column_height - new_y
            elif prev_y > new_y and largest_lhs_column_index == prev_x:
                collection_buffer+= largest_lhs_column_height - new_y
            elif prev_y == new_y and new_y!=largest_lhs_column_height:
                collection_buffer+= largest_lhs_column_height - new_y
                
            # if prev_x is not None:
            # else:
            #     collection_buffer+= largest_lhs_column_height - new_y
            
        elif new_y > largest_lhs_column_height:
            if prev_y !=0:
                collection_buffer+= largest_lhs_column_height - prev_y
            # print("trapping Watter Bro",collection_buffer,new_x,trapped_units)
            trapped_units+=collection_buffer
            collection_buffer = 0
            largest_lhs_column_index,largest_lhs_column_height = new_x,new_y
        
        prev_x,prev_y = new_x,new_y
    # print("Before Sending Collection Buffer : ",collection_buffer)
    return trapped_units


for test_case,expected_op in test_cases:
    op = trap_water(test_case)
    print(test_case,op,expected_op,op == expected_op)
