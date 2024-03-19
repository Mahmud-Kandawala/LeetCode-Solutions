class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1) #Creates a set named seen containing all the unique elements from nums1

        res = [] #Store the intersecting elements found in both nums1 and nums2

        for n in nums2: #Loop iterates through each element n in nums2
            if n in seen: #n is an intersecting element
                res.append(n) #Appended to the res list
                seen.remove(n) #Remove n from the seen set
        return res

   
        
