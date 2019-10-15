from typing import List

def create_splits(loads):
    resource_1 = []
    resource_2 = []
    if loads.__len__() == 1:
        return loads[0]
    
    if loads.__len__() == 2:
        return abs(loads[0] - loads[1])

    loads.sort(reverse=True)
    for i  in range(0,loads.__len__()):
        load = loads[i]
        if sum(resource_1) > sum(resource_2):
            resource_2.append(load)
        else:
            resource_1.append(load)

    return abs((sum(resource_1) - sum(resource_2)))





# A = [1,2,3,4,3,4,4,6,7]
# A = [1,2,3,4,5,4,2,1,3,10]
# A = [,2,3]
# A = [1,1,1,1]
A = [1,2]
print(create_splits(A))

