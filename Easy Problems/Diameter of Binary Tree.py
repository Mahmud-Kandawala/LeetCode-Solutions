# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0] # A list with a single element 0. This will store the maximum diameter found during the traversal of the tree. A list is used to allow updates within the nested function.
        
        def dfs(root): # Helper Function
            if not root: # If Null
                return -1
            left = dfs(root.left) # Recursively calls itself for the left and right children of the current node.
            right = dfs(root.right)

            res[0] = max(res[0], 2 + left + right)# Diameter through the current node is calculated as 2 + left + right

            return 1 + max(left, right) # Returns the height of the current node

        dfs(root)
        return res[0]
