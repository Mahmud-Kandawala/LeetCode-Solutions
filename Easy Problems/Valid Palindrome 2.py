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
                skipL = is_palindrome(s, l + 1, r)
                skipR = is_palindrome(s, l, r - 1)
                return skipL or skipR
            l, r = l + 1, r - 1
        
        return True
