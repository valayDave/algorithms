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

# $ POST ORDER = Left, Right, Root
test_cases = [
    (case_1_node,[3,2,1]),
    (case_2_node,[4,3,2,1]),
    (case3_node,[1,3,2]),
    (case4_node,[2,1,3])
]



def postorder_tree_traversal(root:TreeNode) -> List[int]:
    if root is None:
        return []
    root_stack = []
    value_arr = []
    root_buffer = [] # $ Holds the final arrangement of elements. 
    right_stack = []
    while True:
        if root.left is not None:
            # $ Add to the End the Future Root. 
            root_stack.append(root.left)
        
        if root.left is not None:
            # $ This is done so that the way we have added to the front, we can traverse back the same way. 
            # $ Add current Root to Front 
            root_stack.insert(0,root) # Inserting here Because we keep Going down the Tree until there is a left we encounter. 
            root = root_stack.pop()
        else:
            # $ There will come a point where the current_root No Longer has a left. 
            # $ Then keep checking as long as it has right. 
            if root.right is not None:
                # $ Make the Right The Root and start collecting from there. 
                root_stack.insert(0,root)
                # $ Right stack created so that when adding the nodes to the root_buffer we know what exists on the right. 
                right_stack.insert(0,root)
                root = root.right
            else:
                current_root = root
                # $ As there is no more right or left to this node add it to root_buffer
                value_arr.append(current_root.val)
                
                if len(root_stack) > 0:
                    root_not_found = True
                    while root_not_found and len(root_stack) > 0:
                        # $ extract the root of the node from the root_stack
                        new_root = root_stack.pop(0)
                        # $ see if nodes present in the Root stack have a right because the left for that has been explored. 
                        print("Checking ",new_root.val,root.val)
                        # $ Check if the node extracted is not in the right stack and is not None
                        # $ We check the right stack because we come to this step when we have no
                        # $ more left or right. So we could have even come here from the right instead of just left. 
                        if new_root.right is not None and new_root not in right_stack:
                            # print("The New Root is Not In right Stack and is not None")
                            # print("Breaking to iterate again",list(map(lambda a:a.val,root_buffer)),list(map(lambda a:a.val,root_stack)),new_root.right.val,new_root.val)
                            # $ If am a node whose right has never been encountered before than I will add it to 
                            # $ root_stack and to right_stack so that this same node doesn't come back again.   
                            root_stack.insert(0,new_root)
                            right_stack = [new_root]
                            root = new_root.right
                            root_not_found = False
                            break
                        else:
                            value_arr.append(new_root.val)
                            
                    # $ If there were no right nodes found while traversing back to the root then break. 
                    if root_not_found:
                        break
                else:
                    break
    return value_arr


def printPostorder(root): 
	if root: 

		# First recur on left child 
		printPostorder(root.left) 
		# now recur on right child 
		printPostorder(root.right) 

		# then print the data of node 
		print(root.val)


failed_count = 0
for test_case,expected_op in test_cases:
    op = list(postorder_tree_traversal(test_case))
    # printPostorder(test_case)
    print('\n')
    if op == expected_op:
        continue
    else:
        failed_count+=1
        print("Test Case Failed  : ",op,expected_op,op == expected_op,'\n')
        # printPostorder(test_case)

print("Test Cases Failed : ", failed_count)
print("Test Cases Passed : ", len(test_cases) -failed_count)