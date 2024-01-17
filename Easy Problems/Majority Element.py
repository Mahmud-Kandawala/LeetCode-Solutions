class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {} #A HashMap (dictionary in Python) to keep track of the frequency of each element in nums.
        result, maxCount = 0, 0 # Res = Will hold the most frequent element in nums. Max = Tracks the highest frequency of any element encountered so far.
        
        for n in nums: #Iterates over each element n in the list nums.
            count[n] = 1 + count.get(n, 0) #For each n, it increments its count in the count dictionary. count.get(n, 0) retrieves the current count of n, defaulting to 0 if n is not in count. 
            if count[n] > maxCount: #If the frequency of n (count[n]) is greater than maxCount 
                result = n #result is updated to n
            else: 
                result # Otherwise, result remains unchanged.
            maxCount = max(count[n], maxCount) #Is updated to be the larger of its current value or the frequency of n.
        return result

        
