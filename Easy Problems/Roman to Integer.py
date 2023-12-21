class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman = {"I": 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, 
                    "D" : 500, "M" : 1000}

        result = 0 

        for i in range(len(s)): #This loop iterates through each character in the string s.
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]: #Checks if the current character (s[i]) is followed by a higher-valued character
                result -= roman[s[i]] #If the current character is followed by a higher-valued character, it subtracts the value of the current character from result
            else:
                result += roman[s[i]] #Otherwise, it adds the value of the current character to result
            
        return result

# Note: 
''' The expression i + 1 < len(s) is a bounds check. It ensures that the index i + 1 does not go beyond the length of the string s. 
Remember, i is the current index in the loop iterating over the string. This check is necessary because the code is accessing s[i + 1] in the next part of the condition. 
If i + 1 were equal to or greater than len(s), it would result in an IndexError since it would be trying to access a character outside the range of the string. i = 0...
'''
