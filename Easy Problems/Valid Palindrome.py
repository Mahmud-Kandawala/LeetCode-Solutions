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


#Demo:
"""
Example String
"A man, a plan, a canal: Panama"

Step 1: Initialize Pointers
l, r = 0, len(s) - 1
l is initialized to 0, pointing to the first character 'A'.
r is initialized to len(s) - 1, which is 30, pointing to the last character 'a'.

Step 2: Enter the Main Loop
The condition while l < r is checked. Since l is 0 and r is 30, the loop starts.

Step 3: Skip Non-Alphanumeric Characters on the Left
The inner loop while l < r and not self.alphaNum(s[l]): l += 1 checks if the character at l is non-alphanumeric. For the first character 'A', it is alphanumeric, so l stays at 0.

Step 4: Skip Non-Alphanumeric Characters on the Right
Similarly, while r > l and not self.alphaNum(s[r]): r -= 1 checks if the character at r is non-alphanumeric. The first time, it points to 'a', which is alphanumeric, so r stays at 30.

Step 5: Compare Characters
The code now compares s[l].lower() and s[r].lower(), which are 'a' and 'a' after lowercasing. They match, so the loop continues.

Step 6: Move Pointers
l, r = l + 1, r - 1 moves l to 1 and r to 29, effectively narrowing the window of characters to check next.

Steps 3 to 6 Repeat
These steps repeat, with the loop skipping over spaces and punctuation. Each time, it compares the next pair of alphanumeric characters:
Next, l moves to point at 'm' and r moves to point at 'm', both are compared and match.
This process continues, skipping over non-alphanumeric characters like spaces and commas, and comparing the characters on both ends of the string.

Final Iteration
Eventually, l and r will meet in the middle of the string, after successfully comparing all the alphanumeric characters. In our example, this happens after comparing the n from "plan" and the a from "a canal", since the middle of the string, "a canal: Panama", has been mirrored without considering the colon and spaces.
Once l is not less than r, the loop exits.

Step 7: Return True
Since all comparisons of alphanumeric characters (ignoring cases) matched, the function returns True, indicating the string is a palindrome by the criteria set forth in the function.
"""       
