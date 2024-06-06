# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # If doesn't exist 
            return None
        
        #swap the children
        tmp = root.left # Store the left child of root in a temporary variable tmp
        root.left = root.right # Assign the right child of root to its left child
        root.right = tmp # Assign tmp (which holds the original left child) to the right child of root.

        self.invertTree(root.left) # Recursively call invertTree
        self.invertTree(root.right) # Recursively call invertTree
        return root #Return the new root of the entire tree 

        

        
