'''
    Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

    Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

    0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
    F.length >= 3;
    and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
    Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

    Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

    Example 1:

    Input: "123456579"
    Output: [123,456,579]
    Example 2:

    Input: "11235813"
    Output: [1,1,2,3,5,8,13]
    Example 3:

    Input: "112358130"
    Output: []
    Explanation: The task is impossible.
    Example 4:

    Input: "0123"
    Output: []
    Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
    Example 5:

    Input: "1101111"
    Output: [110, 1, 111]
    Explanation: The output [11, 0, 11, 11] would also be accepted.
    Note:

    1 <= S.length <= 200
    S contains only digits
'''

test_cases = [
                ('0123', []), 
                ('11235813',[1, 1, 2, 3, 5, 8, 13]), 
                ('112358130',[]),
                # ('1101111',[110, 1, 111]), 
                ("1011",[1, 0, 1, 1]), 
                ("0000",[0, 0, 0, 0]),
                ('123456579',[123,456,579]),
                ("0224",[0,2,2,4]),
                ("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511",[]),
                ("502113822114324228146342470570616913086148370223967883880490627727810157768164350462659281443027860696206741126485341822692082949177424771869507721046921249291642202139633432706879765292084310",[])
]

MAX_VAL = 2**32

def generate_fibonacci(string1: str):
    if string1.__len__() < 3:
        return []

    for i in range(string1.__len__()):
        if i == 0:
            continue
        curr_char = string1[i]
        # print('\n',string1[:i],string1[i:],'\n')
        num_1 = int(string1[:i])
        if string1[:i][0] == '0' and i > 1:
            return []
        sub_str = string1[i:]
        num_2 = None
        num_3_str = None
        summing_sequence = False
        j = 1
        summing_start = None
        summed_arr = []
        # for j in range(1,sub_str.__len__()+1):
        while j < sub_str.__len__():
            if j == 1 or summing_sequence == False:
                num_2 = int(sub_str[:j])
            num_3_str = str(num_1 + num_2)
            sequence_follow = sub_str[j:j+num_3_str.__len__()]
            # print(num_1,num_2,num_3_str, sequence_follow,j,sub_str.__len__(),sub_str,summing_start,j)
            if sequence_follow == num_3_str and (num_1 <= ((2**31)-1) and num_2 <= ((2**31)-1) and int(num_3_str) <= ((2**31)-1)):
                # ! No Starting Zeros.
                # ! No Tailing Zeros.
                if summing_sequence is False:
                    summed_arr += [num_1, num_2, int(num_3_str)]
                    # print("Added ::: ",summed_arr)
                    summing_sequence = True
                    summing_start = j
                else:
                    summed_arr += [int(num_3_str)]
                num_1 = int(num_2)
                num_2 = int(num_3_str)
                j += num_3_str.__len__()
            else:
                if summing_sequence is True:
                    j = summing_start+1
                    summing_start = None
                    summing_sequence = False
                    num_1 = int(string1[:i])
                    summed_arr = []
                    continue
                j += 1

        if summing_sequence == True:
            return summed_arr
    return []

for test_case,op in test_cases:
    final_val = generate_fibonacci(test_case)
    print(test_case,final_val,op,final_val == op)
