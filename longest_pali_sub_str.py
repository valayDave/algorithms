s = "134532"

def find_pali2(s:str):
    half_length = (s.__len__()//2)
    chunks = [s[0:half_length],s[half_length+1:s.__len__()+1]]

    print(chunks)


def isPalindrome(str1): 
    # Run loop from 0 to len/2  
    for i in range(0, len(str1)//2):  
        if str1[i] != str1[len(str1)-i-1]: 
            return False
    return True

def find_pali(s:str):
    largest = ''
    current = None
    if s.__len__() == 1:
        return s
    for i in range(0,s.__len__()):
        for j in range(i+1,s.__len__()+1):
            current = s[i:j]
            if current[0] == current[-1]:
                # if isPalindrome(current):
                if current == current[::-1]:
                    # Means is a palindrome 
                    if len(current) > len(largest):
                        largest = current  

    # print(max(largest, key=len))
    # print(largest)
    if largest.__len__() > 0:
        return largest
    else:
        return ''



print(find_pali(s))