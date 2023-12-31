class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = 1 #Keep track of the position in the list nums

        for r in range(1,len(nums)): # Iterate over the indices of the list nums, starting from index 1 (the second element) to the last index. The variable r represents the current index in the loop.
            if nums[r] != nums[r-1]: #Checks if the current element (nums[r]) is different from the previous element 
                nums[l] = nums[r] #Assign the value of nums[r] to nums[l]
                l += 1 #To move the position for the next unique element.
        
        return l #Represent the new length of the modified list.
