def time_gen(time:str):
    time_arr = time.split(':')
    hour_string = time_arr[0]
    min_string = time_arr[1]
    final_string = ''
    if hour_string[0] == '?' and hour_string[1] == '?':
        final_string+='23'
    elif hour_string[0] == '?' and hour_string[1] != '?':
        if int(hour_string[1]) <= 3:
            final_string+=('2'+hour_string[1])
        else:
            final_string+=('1'+hour_string[1])
    elif hour_string[0] != '?' and hour_string[1] == '?':
        if int(hour_string[0]) == 2:
            final_string+=(hour_string[0]+'3')
        else:
            final_string+=(hour_string[0]+'9')
    else:
        final_string+=hour_string

    final_string+=':'
    
    if min_string[0] == '?' and min_string[1] == '?':
        final_string+='59'
    elif min_string[0] == '?' and min_string[1] != '?':
        final_string+=('5'+min_string[1])

    elif min_string[0] != '?' and min_string[1] == '?':
        final_string+=(min_string[0]+'9')
    else:
        final_string+=min_string
    return final_string


test_cases = [("2?:?8","23:58"),("?8:4?","18:49"),("??:??","23:59"),("06:34","06:34"),('1?:?4','19:54'),('2?:3?','23:39'),('?7:??','17:59'),]
for test_case,expected_op in test_cases:
    op = time_gen(test_case)
    print(test_case,op,expected_op,op == expected_op)