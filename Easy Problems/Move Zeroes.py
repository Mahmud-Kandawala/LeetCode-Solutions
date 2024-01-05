class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 #Initializes a variable l (left pointer) to 0. It is used to track the position where a non-zero element should be placed
        for r in range(len(nums)): #r is a variable that takes values from 0 to the length of the list nums minus one. It serves as the right pointer, moving through each element of the list
            if nums[r]: #Checks if the current element at index r is non-zero
                nums[l], nums[r] = nums[r], nums[l] #If the current element is non-zero, it is swapped with the element at index l. This effectively moves the non-zero element to the front part of the list
                l +=1 #After a swap, l is incremented. This ensures that subsequent non-zero elements are placed after the already moved non-zero elements
        return nums      
