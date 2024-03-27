class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0 #Store the result of the square root

        while l <= r: #Continues as long as the r is greater than or equal to l
            m = l + ((r-1) // 2) #The aim is to avoid overflow and correctly adjust the middle calculation within search space
            if m*m > x: #If square greater than x, integer to the left of m
                r = m - 1 #Right bound of the search interval updated to one less, to narrow down the search space to the left
            elif m*m < x: #If square less than x, integer square root is either m or to the right of m.
                l = m + 1 #Left bound of search interval is updated to one more than m to narrow down the search to the right
                res = m # Result is updated to m since m largest known integer so far whose square is less than or equal to x
            else:
                return m
        return res # If the loop exits without finding an exact square root (when m**2 is not equal to x), the method returns res. This value is the largest integer whose square is less than or equal to x, determined during the search process.


        
