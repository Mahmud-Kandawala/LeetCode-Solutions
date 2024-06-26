class Solution(object):
    def isBalanced(self, root):

        #If the node is null, it's balanced and its height is 0
        def dfs(root):
            if not root: return[True, 0]

            left, right = dfs(root.left), dfs(root.right) #Recursively check the left/right subtree
            '''
                The variable balanced is calculated based on conditions:
                - left[0] & right[0]: The subtree is balanced. (booleans)
                - abs(left[1] - right[1]) <= 1: The height difference (integers)
                - If all ANDS are True, balanced will be True
            '''
            balanced = (left[0] and right[0] and 
                abs(left[1] - right[1]) <= 1)

            
            return [balanced, 1 + max(left[1], right[1])] #Whether the current subtree, The height of the current subtree. It is 1 (for the current node) plus the maximum height of the left and right subtrees.
        
        return dfs(root)[0] #Returns the first element of the result, indicating whether the entire tree is balanced.


        
        
