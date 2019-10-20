"""
    # Binary Tree : inorder traversal --> left,root,right     
    # Lefts go to Q, Rights go to stack. Pop stack stack when you progress a level up from
    # a certain node. 
"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

case_1_node = TreeNode(1)
case_1_node.left = None
case_1_node.right = TreeNode(2)
case_1_node.right.left = TreeNode(3)

case_2_node = TreeNode(1)
case_2_node.left = TreeNode(4)
case_2_node.right = TreeNode(2)
case_2_node.right.left = TreeNode(3)


case3_node = TreeNode(2)
case3_node.left = TreeNode(3)
case3_node.right = None
case3_node.left.left = TreeNode(1)

# [3,1,null,null,2]
case4_node = TreeNode(3)
case4_node.left = TreeNode(1)
case4_node.right = None
case4_node.left.left = None
case4_node.left.right = TreeNode(2)


test_cases = [
    (case_1_node,[1,3,2]),
    (case_2_node,[4,1,3,2]),
    (case3_node,[1,3,2]),
    (case4_node,[1,2,3])
]

def inorder_tree_traversal(root:TreeNode) -> List[int]:
    if root is None:
        return []
    root_stack = []
    value_arr = []
    while True:
        if root.left is not None:
            # $ Add to the End the Future Root. 
            root_stack.append(root.left)
        
        if root.left is not None:
            # print("This Means that the next Node we Treat should be a left node",len(rhs_stack),len(root_stack))
            
            # $ Add current Root to Front 
            # $ This is done so that the way we have added to the front, we can traverse back the same way. 
            root_stack.insert(0,root) # Inserting here Because we keep Going down the Tree until there is a left we encounter. 
            root = root_stack.pop()
        else:
            # $ There will come a point where the current_root No Longer has a left. 
            # z = list(map(lambda a:a.val,root_stack))
            # $ 1. add current_root.value to the value_arr
            value_arr+=([root.val])
            # $ 2. if this current_root has an RHS. 
            if root.right is not None:
                # print("This Means that There is a Right.")
                # $ Make the Right The Root and start collecting from there. 
                root = root.right
            else:
                # $ As there is no more right or left to this node check the root_stack
                # print("Adding Root Stack to Value Arr",value_arr,z,len(root_stack))
                if len(root_stack) > 0:
                    not_found_root = True
                    while not_found_root and len(root_stack) > 0:
                        new_root = root_stack.pop(0)
                        value_arr+=[new_root.val]
                        # print("After Adding From Root Stack",value_arr,new_root.val)
                        # $ see if nodes present in the Root stack have a right. 
                        if new_root.right is not None:
                            root = new_root.right
                            # print("Setting New Right root : ",root.val)
                            # $ If there is a right to the node the set that as the root and start collecting. 
                            not_found_root = False
                    # $ If there were no right nodes found while traversing to the root then break. 
                    if not_found_root:
                        break
                else:
                    break
    return value_arr


def printInorder(root): 
	if root: 

		# First recur on left child 
		printInorder(root.left) 

		# then print the data of node 
		print(root.val), 

		# now recur on right child 
		printInorder(root.right) 

failed_count = 0
for test_case,expected_op in test_cases:
    op = list(inorder_tree_traversal(test_case))
    print('\n')
    if op == expected_op:
        continue
    else:
        failed_count+=1
        print("Test Case Failed  : ",op,expected_op,op == expected_op,'\n')
        printInorder(test_case)

print("Test Cases Failed : ", failed_count)
print("Test Cases Passed : ", len(test_cases) -failed_count)