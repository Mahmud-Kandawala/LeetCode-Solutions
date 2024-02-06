class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  #Initializes two pointers, l (left) and r (right), at the start and end of the string.

        while l < r: #Continues until the two pointers meet or cross each other. 
            while l < r and not self.alphaNum(s[l]): #Skips non-alphanumeric characters by moving the left pointer towards the right until an alphanumeric character is found. l < r checks if l is inbound. 
                l+= 1 #Skips spaces 
            
            while r > l and not self.alphaNum(s[r]):
                r-= 1 

            if s[l].lower() != s[r].lower(): #Compares the current characters pointed by l and r after converting them to lowercase. If they are not equal, it means the string is not a palindrome, and the method returns False
                return False
            
            l,r = l + 1, r - 1 #Moves the l pointer to the right and the r pointer to the left to continue the comparison with the next set of characters.
        
        return True

    
    # Checking ASCII Value:
    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))
