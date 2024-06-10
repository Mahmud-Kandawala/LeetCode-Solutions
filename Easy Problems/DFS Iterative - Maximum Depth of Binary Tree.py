# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS Iterative (Pre-Order)
        
        stack = [[root, 1]] #Initialized with a list containing a tuple [root, 1], where root is the starting node and 1 is the initial depth.
        res = 0 #Keep track of the maximum depth encountered during the traversal.
       
        while stack: # Not empty
            node, depth = stack.pop() #Removes the top element from the stack. node is the current node being processed, and depth is its depth in the tree.

            if node: # Not Null
                res = max(res, depth)
                stack.append([node.left, depth + 1]) #Adds the left child of the current node to the stack with an incremented depth.
                stack.append([node.right, depth + 1]) # Same as above
            
        return res 



        
