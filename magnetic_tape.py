import numpy as np, numpy.random
from typing import List,Tuple
import random
import functools

ROUNDING_FIGURE = 2
 
# $ @returns : [(prog_index,prog_length,prog_probability)]
def create_tape(tape_size = 10,len_min= 5,len_max= 30):
    # $ pi is the probability of loading a program. 
    pi_values = np.random.dirichlet(np.ones(tape_size),size=1) # 10 Elem array where Numbers sum up to one.  
    # $ li is the length of a program 
    li_values = np.random.randint(low = len_min, high = len_max, size = tape_size)
    # $ i is the index of the program
    i_values = [i for i in range(tape_size)]
    pi_values = [round(float(i),ROUNDING_FIGURE) for i in pi_values[0]]
    tape_programs = list(zip(i_values,li_values,pi_values))
    return tape_programs

# $ shuffle_tape : reorders the elements randomly . 
def shuffle_tape(tape:List[Tuple[int,int,float]]):
    new_tape = list(tape)
    for i in range(len(new_tape)):
        swap_index = random.randint(0,len(tape)-1)
        new_tape[i],new_tape[swap_index] = new_tape[swap_index],new_tape[i]
    return new_tape

def avg_time_to_load_program(tape:List[Tuple[int,int,float]]):
    T_sum = 0
    for i in range(len(tape)):
        prog_index,prog_length,prog_probability = tape[i]
        sum_of_tapes = 0
        for j in range(i+1):
            sum_of_tapes+=tape[j][1]
        T_sum+=(prog_probability*float(sum_of_tapes))
    return round(T_sum,ROUNDING_FIGURE)

def get_fact(num):
    return functools.reduce(lambda a,b:a*b,list(range(1,num+1)))

def get_min_configuration(tape_programs:List[Tuple[int,int,float]]):
    progs = list(tape_programs)        
    min_configuration = None
    num_combinations = get_fact(len(progs))
    for i in range(num_combinations):
        shuffled_tape = shuffle_tape(progs)
        avg_time = avg_time_to_load_program(shuffled_tape)
        # print(avg_time)
        if min_configuration is None:
            min_configuration = (shuffled_tape,avg_time)
        else:
            if min_configuration[1] > avg_time : 
                min_configuration = (shuffled_tape,avg_time)
    return min_configuration


# $ programs are stored in the order of the increasing values of li^3
# $ @returns : sorted(tape_programs)
def case_1(tape_programs):
    return sorted(tape_programs, key=lambda tup: tup[1]**3)

# $  programs are stored in the order of the decreasing values of pi^2
# $ @returns : sorted(tape_programs)
def case_2(tape_programs):
    return sorted(tape_programs, key=lambda tup: tup[2]**2,reverse=True)

# $ the programs are stored in the order of the decreasing values of (pi/li)^2
# $ @returns : sorted(tape_programs)
def case_3(tape_programs):
    return sorted(tape_programs, key=lambda tup: (tup[2]/tup[1])**2,reverse=True)

def create_test_cases():
    tape_programs = create_tape(tape_size =4)
    optimal_soln = get_min_configuration(tape_programs)

    print(tape_programs,'\n')
    print("Best Configuration : ",optimal_soln[0],'\n')
    print("Value : ",optimal_soln[1],'\n')

    case_1_tape = case_1(tape_programs)
    case_2_tape = case_2(tape_programs)
    case_3_tape = case_3(tape_programs)

    print("Case 1 Solution ! ",avg_time_to_load_program(case_1_tape),case_1_tape,'\n')
    print("Case 2 Solution ! ",avg_time_to_load_program(case_2_tape),case_2_tape,'\n')
    print("Case 3 Solution ! ",avg_time_to_load_program(case_3_tape),'\n')
    print('\n\n')

    return (tape_programs,optimal_soln,avg_time_to_load_program(case_1_tape),avg_time_to_load_program(case_2_tape),avg_time_to_load_program(case_3_tape))

for i in range(6):
    tape_programs,optimal_soln,avg_time_to_load_case_1_tape,avg_time_to_load_case_2_tape,avg_time_to_load_case_3_tape = create_test_cases()
    if avg_time_to_load_case_3_tape > optimal_soln[1]:
        print("Found Edge Case For 3!")
        print(tape_programs,'\n')
        print("Best Configuration : ",optimal_soln[0],'\n')
        print("Best Configuration Value : ",optimal_soln[1],'\n')
        print("Case 3 Solution ! ",avg_time_to_load_case_3_tape,'\n')



