class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set() # A set that will be used to keep track of unique characters in the current substring
        
        l = 0 # An integer representing the left pointer of the current substring
        
        res = 0 # : An integer representing the result or the length of the longest substring without repeating characters

        for r in range(len(s)): # This initiates a loop that iterates over the indices of the input string s
            
            while s[r] in charSet: # This initiates a nested loop that runs as long as the character at index r of the string s is already present in the charSet
                
                charSet.remove(s[l]) # The character at index l in the string s is removed from the charSet to eliminate the repetition in the current substring
                
                l += 1 # The left boundary l is incremented to consider the next possible substring
            
            charSet.add(s[r]) # The character at index r in the string s is added to the charSet, as it represents the next character in the current substring
            res = max(res, r - l + 1) # Updates the res variable to contain the length of the longest substring without repeating characters found so far
        
        return res # Once the loop finishes, the method returns the variable res, which holds the length of the longest substring without repeating characters


# Notes: 

"""
Step-by-Step Execution:

Initialize the charSet set, the left pointer l to 0, and the result res to 0.

Start iterating through the input string "abcabcbb" using the right pointer r.

r = 0: Current character is 'a'.

Add 'a' to charSet (charSet = {'a'}), and calculate the length of the current substring: r - l + 1 = 0 - 0 + 1 = 1.
Update res to the maximum value between res (0) and the current length of the substring (1), so res becomes 1.
r = 1: Current character is 'b'.

Add 'b' to charSet (charSet = {'a', 'b'}), and calculate the length of the current substring: r - l + 1 = 1 - 0 + 1 = 2.
Update res to the maximum value between res (1) and the current length of the substring (2), so res becomes 2.
r = 2: Current character is 'c'.

Add 'c' to charSet (charSet = {'a', 'b', 'c'}), and calculate the length of the current substring: r - l + 1 = 2 - 0 + 1 = 3.
Update res to the maximum value between res (2) and the current length of the substring (3), so res becomes 3.
r = 3: Current character is 'a'.

The character 'a' is already in charSet, so the while loop is entered.
Remove 'a' from charSet, so charSet becomes {'b', 'c'}, and increment l to 1.
Now, the substring from index l to index r is 'bca'.
The length of the current substring is r - l + 1 = 3 - 1 + 1 = 3.
Update res to the maximum value between res (3) and the current length of the substring (3), so res remains 3.
r = 4: Current character is 'b'.

The character 'b' is already in charSet, so the while loop is entered.
Remove 'b' from charSet  , so charSet becomes {'c'}, and increment l to 2.
Now, the substring from index l to index r is 'cab'.
The length of the current substring is r - l + 1 = 4 - 2 + 1 = 3.
Update res to the maximum value between res (3) and the current length of the substring (3), so res remains 3.
r = 5: Current character is 'c'.

The character 'c' is already in charSet, so the while loop is entered.
Remove 'c' from charSet, so charSet becomes an empty set ({}), and increment l to 3.
Now, the substring from index l to index r is 'abb'.
The length of the current substring is r - l + 1 = 5 - 3 + 1 = 3.
Update res to the maximum value between res (3) and the current length of the substring (3), so res remains 3.
r = 6: Current character is 'b'.

The character 'b' is not in charSet, so it is added to charSet (charSet = {'b'}), and calculate the length of the current substring: r - l + 1 = 6 - 3 + 1 = 4.
Update res to the maximum value between res (3) and the current length of the substring (4), so res becomes 4.
r = 7: Current character is 'b'.

The character 'b' is already in charSet, so the while loop is entered.
Remove 'b' from charSet, so charSet becomes an empty set ({}), and increment l to 4.
Now, the substring from index l to index r is 'abb'.
The length of the current substring is r - l + 1 = 7 - 4 + 1 = 4.
Update res to the maximum value between res (4) and the current length of the substring (4), so res remains 4.
The iteration through the string is complete, and the method returns the final value of res, which is 4. This represents the length of the longest substring without repeating characters in the input string "abcabcbb", and the substring is 'abcb'.

"""
