class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # m = number of elements in nums1
        # n = number of elements in nums2

       
        last = m + n - 1  #Last index nums1

        #Merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]: 
                nums1[last] = nums1[m - 1] #If the current element in nums1 is greater, It is placed at the last position of nums1
                m -=1 #m is decremented to move to the previous element of nums1
            else:
                nums1[last] = nums2[n - 1] #The current element in nums2 is greater or equal, it is placed at the last position of nums1
                n -= 1 #n is decremented to move to the previous element of nums2
            last -= 1 #Last index is decremented to fill the next position in the next iteration

        
#Fill nums1 with leftover nums2, this means nums1's elements have been completely merged, and only nums2's elements are left to be placed in nums1. This is done in the following while loop:
        while n > 0:
            nums1[last] = nums2[n - 1] #Each element from nums2 is placed in the corresponding position in nums1, and both
            n, last = n - 1, last - 1 #n and last are decremented to move to the previous elements     
