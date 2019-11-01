'''
Interval Scheduling. 
Goal: find maximum subset of mutually compatible jobs.
Job  J = {start_time,finish_time}
'''
import numpy
import random 

MAX_HIGH_BOUND = 100
def get_time_bound(index):
    start_time = random.randint(0,MAX_HIGH_BOUND-2)
    end_time = random.randint(start_time,MAX_HIGH_BOUND)
    return (index,start_time,end_time) 

def get_test_case():
    return [get_time_bound(i) for i in range(5)]

test_cases = [get_test_case() for i in range(20)]

# test_case = [get_time_bound(i) for i in range(10)]
# test_case = [(0, 69, 74), (1, 80, 91), (2, 16, 75), (3, 95, 96), (4, 18, 40), (5, 20, 23), (6, 37, 42), (7, 95, 97), (8, 41, 82), (9, 38, 75)]
# print(test_case)

def check_compatible(time_arr,time_tuple):
    compare_index,compare_start,compare_end = time_tuple
    for index,start_time,end_time in time_arr:
        if compare_start < end_time: # and ends before 
            return False
    return True

def check_compatible_new(time_arr,time_tuple):
    compare_index,compare_start,compare_end = time_tuple
    for index,start_time,end_time in time_arr:
        if start_time < compare_start and end_time > compare_start:
            return False
        if start_time > compare_start and compare_end > start_time: # and ends before 
            return False
        if start_time == compare_start or start_time == compare_end:
            return False

    return True

def case1(time_arr):
    start_time_descending = sorted(time_arr, key=lambda tup: tup[1],reverse=True)
    mutually_compatible_jobs = []
    mutually_compatible_jobs_set = set()
    for time_tuple in start_time_descending:
        if check_compatible_new(mutually_compatible_jobs,time_tuple):
            mutually_compatible_jobs.append(time_tuple)
            mutually_compatible_jobs_set.add(time_tuple[0]) # Adds the index
    return mutually_compatible_jobs_set

def case2(time_arr):
    length_descending = sorted(time_arr, key=lambda tup: tup[2]-tup[1],reverse=True)
    # print(length_descending)
    # print(list(map(lambda tup:tup[2]-tup[1],length_descending)))
    mutually_compatible_jobs = []
    mutually_compatible_jobs_set = set()
    for time_tuple in length_descending:
        if check_compatible_new(mutually_compatible_jobs,time_tuple):
            mutually_compatible_jobs.append(time_tuple)
            mutually_compatible_jobs_set.add(time_tuple[0]) # Adds the index
    return mutually_compatible_jobs_set

def case3(time_arr):
    reciprocal_length_ascending = sorted(time_arr, key=lambda tup: float(1)/float(tup[2]-tup[1]))
    # print(reciprocal_length_ascending)
    # print(list(map(lambda tup:float(1)/float(tup[2]-tup[1]),reciprocal_length_ascending)))
    mutually_compatible_jobs = []
    mutually_compatible_jobs_set = set()
    for time_tuple in reciprocal_length_ascending:
        if check_compatible_new(mutually_compatible_jobs,time_tuple):
            mutually_compatible_jobs.append(time_tuple)
            mutually_compatible_jobs_set.add(time_tuple[0]) # Adds the index
    return mutually_compatible_jobs_set

def optimal_schedule(time_arr):
    finish_time_ascending = sorted(time_arr, key=lambda tup: tup[2])
    mutually_compatible_jobs = []
    mutually_compatible_jobs_set = set()
    for time_tuple in finish_time_ascending:
        if check_compatible_new(mutually_compatible_jobs,time_tuple):
            mutually_compatible_jobs.append(time_tuple)
            mutually_compatible_jobs_set.add(time_tuple[0]) # Adds the index
    return mutually_compatible_jobs_set


final_test_cases = [ (test_case,optimal_schedule(test_case)) for test_case in test_cases ]

for test_case,expected_op in final_test_cases:
    op = case3(test_case)
    if len(expected_op) != len(op):
        print(test_case)
        print(expected_op,op,'\n\n')

    