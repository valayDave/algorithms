'''
    Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

    You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

    Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

    For the last line of text, it should be left justified and no extra space is inserted between words.

    Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.
    Example 1:

    Input:
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    Output:
    [
    "This    is    an",
    "example  of text",
    "justification.  "
    ]
    Example 2:

    Input:
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    Output:
    [
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
    ]
    Explanation: Note that the last line is "shall be    " instead of "shall     be",
                because the last line must be left-justified instead of fully-justified.
                Note that the second line is also left-justified becase it contains only one word.
    Example 3:

    Input:
    words = ["Science","is","what","we","understand","well","enough","to","explain",
            "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    Output:
    [
    "Science  is  what we",
    "understand      well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "
    ]s
'''
from typing import List


# class Solution:
#     def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
#         print("Here",words[0],maxWidth)
PADDING_SPACE = ' '
def justify_left(word_arr:List[str],max_width:int):
    building_string = []
    curr_sent = None
    if len(word_arr) == 0:
        return '',[]
    if len(word_arr) == 1:
        building_string+=[word_arr[0]]
        curr_sent = ''.join(building_string)
        assert(len(word_arr[0]) <= max_width) # TO Ensure Putting it in the string.      
        while len(curr_sent) < max_width:
            building_string+=[PADDING_SPACE]
            curr_sent = ''.join(building_string)
        return ''.join(building_string),[]
    for i in range(0,word_arr.__len__()):
        word = word_arr[i]
        if i == 0:
            building_string+=[word,PADDING_SPACE]
            curr_sent = ''.join(building_string)
            continue
        curr_sent = ''.join(building_string)
        if len(curr_sent) > max_width or i == word_arr.__len__()-1:
            if i == word_arr.__len__() - 1 : 
                if len(curr_sent) <= max_width:
                    building_string+=[word,PADDING_SPACE]
                    i+=1 # $ Because we dont want to return this element. 
            # $ Because it is left justified we want to keep the spaces. 
            curr_sent = ''.join(building_string)
            assert(PADDING_SPACE in building_string[-1])
            while len(curr_sent) < max_width:
                building_string[-1]+=PADDING_SPACE
                curr_sent = ''.join(building_string)

            return ''.join(building_string),word_arr[i:]    
        else:
            building_string+=[word,PADDING_SPACE]
        
def justify_full(word_arr:List[str],max_width:int):
    building_string = []
    curr_sent = None
    if len(word_arr) == 0:
        return '',[]
    if len(word_arr) == 1:
        building_string+=[word_arr[0]]
        curr_sent = ''.join(building_string)
        assert(len(word_arr[0]) <= max_width) # TO Ensure Putting it in the string.      
        while len(curr_sent) < max_width:
            building_string+=[PADDING_SPACE]
            curr_sent = ''.join(building_string)
        return ''.join(building_string),[]      

    for i in range(0,word_arr.__len__()):
        word = word_arr[i]
        if i == 0:
            building_string+=[word,PADDING_SPACE]
            curr_sent = ''.join(building_string+[word])     
            continue
        
        curr_sent = ''.join(building_string+[word])     
        # print(curr_sent,len(curr_sent),building_string,max_width)
        if len(curr_sent) > max_width or i == word_arr.__len__()-1:
            if i == word_arr.__len__()-1: 
                if len(curr_sent) <= max_width:
                    building_string+=[word,PADDING_SPACE]
                    i+=1 # $ Because we dont want to return this element. 

            if PADDING_SPACE in building_string[-1] and building_string.__len__() > 2:
                building_string.pop() # $ Remove the last Element if Space only when there are more than 1 one words to print. 
            
            padding_indexes = [j for j, x in enumerate(building_string) if PADDING_SPACE in x]
            k = 0
            curr_sent = ''.join(building_string)

            while len(curr_sent) < max_width:
                if k == padding_indexes.__len__():
                    k = 0
                # $ Extra spaces between words should be distributed as evenly as possible.
                # $ If the number of spaces on a line do not divide evenly between words, 
                # $ the empty slots on the left will be assigned more spaces than the slots on the right.
                building_string[padding_indexes[k]] += PADDING_SPACE 
                curr_sent = ''.join(building_string)
                k+=1
                # print(''.join(building_string),k,len(curr_sent))
            # $ Ideally now the sentence is constructed 
            return ''.join(building_string),word_arr[i:]
        else:
            building_string+=[word,PADDING_SPACE]

def build_line(word_arr:List[str],max_width:int,justification_type:str)-> (str,List[str]):
    # $ Parameters will have special provisions that process basis the rules of Justification
    building_string = []
    if justification_type is 'left':
        return justify_left(word_arr,max_width)         
    elif justification_type is 'full':
        return justify_full(word_arr,max_width)
    else:
        raise Exception("There Needs to be a type Mentioned Here. ")
    # $ method also returns the elements that got removed. 
    return ('',word_arr)


def full_justify(words:List[str],max_width:int) -> List[str]:
    # $ You should pack your words in a greedy approach; 
        # $ that is, pack as many words as you can in each line. 
        # $ Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
    new_arr = []
    curr_string = ''
    curr_arr = []
    curr_acc = 0
    # for i in range(0,words.__len__()):
    i = 0
    while words.__len__() > 0:
        current_word = words.pop(0) #$ Extracts the First word.
        curr_acc+= current_word.__len__()
        if curr_acc < max_width:
            curr_arr.append(current_word) #$ Append Until you exceed Limit
            curr_acc+=1
        else:
            # $ current_word is not added Yet to acc. so add it back to array and process the new line. 
            curr_arr.append(current_word)
            # print(curr_arr,curr_acc)
            line = None
            residue_data = None
            # words.insert(0,current_word)
            if words.__len__() == 0: #$ This means that I am on the last line and I have exceeded sentence limit. 
                # $ For the last line of text, it should be left justified and no extra space is inserted between words.
                line,residue_data = build_line(curr_arr,max_width,'full')
                # print(line,residue_data)
            else:
                line,residue_data = build_line(curr_arr,max_width,'full')
                # print(line,residue_data)
            words = residue_data + words
            new_arr.append(line)
            curr_arr = []
            curr_acc = 0
            continue

    if curr_arr.__len__() > 0 :
        last_line,residue_data = build_line(curr_arr,max_width,'left')
        new_arr.append(last_line)

    return new_arr
            


# words = ["Listen","to","many,","speak","to","a","few."]
words = ["What"]
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
print(''.join([i+'\n' for i in full_justify(words,20)]))
print(full_justify(["What"],20))