from typing import List
import functools

def row_creation_condition(height:int,student_rows:List[List[int]]):
    # print(student_rows,height)
    if student_rows.__len__() == 0:
        return True,None

    for index,student_row in enumerate(student_rows):
        # $ For the i-th student, if there is a row in which all the students are taller than A[i]
        row_found = functools.reduce(lambda a,b: a & b ,[height < ht for ht in student_row])
        if row_found:
            return False,index
    return True,None

def find_min_rows(heights):
    rows = [] # [[heights]]
    # The students arrive by one, sequentially (as their heights appear in A)
    for height in heights:
        row_creation_bool,row_index =  row_creation_condition(height,rows)
        if row_creation_bool:
            rows+= [[height]]
        else:
            rows[row_index].append(height)
    # print(rows)
    return len(rows)


A = [5, 4, 3, 6, 1]
find_min_rows(A)