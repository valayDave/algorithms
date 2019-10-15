s = "abbaaabcbdefgh"

Palindrome_accumilator = [[-1 for i in range(0,s.__len__())] for i in range(0,s.__len__())]
# def get_inter_val():



def find_pali(s:str,starting_index:int)->int:
    current = None
    num_cuts = 0
    if s.__len__() == 1:
        return 0
    i = 0
    print("Processing : ",s,' With Start Index : ',starting_index)
    while i < s.__len__():
    # for i in range(0,s.__len__()):
        if i == 0 : 
            j = i+1    
        pali_start = False
        add_partition = False
        curr_pali = ''

        if Palindrome_accumilator[starting_index][i] == 1:
            print("FOUND MATCH ::::::::::::::",s[:i])
        
        while j < s.__len__()+1:
            current = s[i:j]
            # print(current)
            if current == '':
                break
            # if Palindrome_accumilator[i][j]    
            if current[0] == current[-1]:
                if current == current[::-1]:
                    # TODO Store this Result Somewhere.
                    # print("Pali Found in Inner Loop.") 
                    # Means is a palindrome 
                    if pali_start is False:
                        pali_start = True
                    curr_pali = current
            else:
                # TODO Store this Result Somewhere. 
                if pali_start is True:
                    # Means the palindrome has ended
                    pali_start = False
                    add_partition = True
            j+=1
        
        if add_partition:
            if i+curr_pali.__len__() != s.__len__():
                print('Palindrome Was Found, Cut Being Added',curr_pali,starting_index+i,i+curr_pali.__len__())
                num_cuts+=1
                Palindrome_accumilator[starting_index+i][i+curr_pali.__len__()] = 1
            # $ Below Value SHould be Stored as a bool. It can help gain absolute value of index from which there was a palindrome    
            i = i+curr_pali.__len__() # $ Datastructure to store in : pali_recorder[start_index][i] = True # This will denote a cut. 
            j = i+1
        else:

            j = i+1
            i+=1
        
    return num_cuts



def find_pali3(s:str)->int:
    min_num = None
    for i in range(0,s.__len__()+1):
        start = s[i:]
        num_from_start = find_pali(start,i)
        end = s[:i]
        num_from_end = find_pali(end,s.__len__()-i)
        print(num_from_start,num_from_end,num_from_start+num_from_end,i,s[i:],len(s[i:]),s[:i],len(s[:i]))
        if min_num is None:
            min_num = num_from_start
        elif (num_from_start+num_from_end+1) < min_num:
            min_num = num_from_start+num_from_end+1
            # print("Changing Minumum : ",min_num,s[i:],s[:i])
    return min_num


# print(Palindrome_accumilator[0][3])
print("Finding : ",s)
print(find_pali3(s))

