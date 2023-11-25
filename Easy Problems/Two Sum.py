class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # Hash Map 

        for i, number in enumerate(nums): # i = index, number = current value in list, enumerate goes through the list tracking the index 
            diff = target - number

            if diff in hashMap: 
                return [hashMap[diff], i] # Returns the diff's index and the current index 
            
            hashMap[number] = i  # If the diff is not found, store the current number and its index in the hashmap

        
        return # If no valid pair is found, return an empty list (this should not happen in the given problem)

# Work 

# Hash Map
# -------------------  >>> nums = [2,7,11,15], target = 9
# Value     Index 
#  2          0


# 9 - 2 = 7, which is not in hash map so store 2 and its index in it 
# 9 - 7 = 2, which IS in the hash map, so return the index of the differnce and the current index (i)

# Output = [0, 1]
