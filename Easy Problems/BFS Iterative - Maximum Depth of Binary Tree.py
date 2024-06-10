# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative BFS
        if not root:
            return 0

        level = 0 #Keep track of the current depth of the tree
        q = deque([root]) #Initialized with the root node
        while q: #Do until q is empty 
            for i in range (len(q)): #Iterates through all nodes currently in the queue
                node = q.popleft() #Removes the leftmost node from the queue and processes it
                if node.left: #If Left Not Null
                    q.append(node.left)
                if node.right: #If Right Not Null
                    q.append(node.right)

            level += 1
        return level


        
        
