class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: #Palindromes can't be negative numbers 
            return False #If so, return False 
        
        divider = 1 #Intializes divider to 1 
        while x >= 10 * divider:
            divider *= 10  
            
#This loop multiplies divider by 10 until it is just smaller than x. It's used to find the highest place value in x
        
        while x: #Will run while x is not 0
            right = x % 10 #Extracts rightmost digit of x
            left = x // divider #Extracts leftmost digit of x
            
            if left != right:
                return False
                
            x = (x % divider) // 10 #Removes the leftmost and rightmost digits from x
            divider = divider / 100 #Adjusts divider for the next iteration, accounting for the two digits removed from x
        
        return True
            
