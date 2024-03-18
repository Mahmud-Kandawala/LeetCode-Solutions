class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0

        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i]) #Character at position is appended
            res.append(word2[j])
            i += 1 #Incremented to move to the next characters
            j += 1 
        res.append(word1[i:]) #Appends the remaining characters 
        res.append(word2[j:]) 
        return "".join(res)
        
