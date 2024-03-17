class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = is_palindrome(s, l + 1, r) #Checks the substring excluding the character at 'l'
                skipR = is_palindrome(s, l, r - 1) #Checks the substring excluding the character at 'r'
                return skipL or skipR #If either returns True, entire is True
            l, r = l + 1, r - 1
        
        return True


"""
How Skipping Works:

So, skipL = is_palindrome(s, l + 1, r) means we're checking the substring "aca" by calling is_palindrome("abca", 2, 2), 
effectively skipping 'b' (because we passed l+1, which is 2, to the function, not directly altering l in the original context). 
It does not mean l and r are at the same position; 
it means we're checking the substring from the character right after l to r, inclusive.

"""
