class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = "" #Initializes a variable result with an empty string. 

        for i in range(len(strs[0])): #Starts a loop that will iterate over the characters of the first string in the strs list.
            for s in strs: #Iterates over each string s in the list strs.
                if i == len(s) or s[i] != strs[0][i]: #Checks if the current index i has reached the end of the current string s or checks if the current character in the string s is different from the corresponding character in the first string of the list.
                    return result 
            result +=  strs[0][i] #If the conditional check fails (meaning the current character is the same in all strings checked so far), this line appends the current character from the first string to result.
        return result 
            

#Just Code:
"""
def longestCommonPrefix(self, strs: List[str]) -> str:
        result = "" 
        
        for i in range(len(strs[0])): 
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]: 
                    return result 
            result +=  strs[0][i] 
        
        return result 
"""      
