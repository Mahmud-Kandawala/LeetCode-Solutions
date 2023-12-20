class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2 #Creates two variables A and B, and assigns nums1 to A and nums2 to B
        total = len(nums1) + len(nums2) #Total is the sum of the lengths of both arrays, 
        half = total // 2 # Half is the integer division of total by 2. This half value is used to find the median position in the combined array.

        if len(B) < len(A):
            A, B = B, A #This block swaps the arrays if B is smaller than A. The algorithm works more efficiently if A is the smaller array.

        l, r = 0, len(A) - 1  #This sets up the initial boundaries for binary search. l is the left boundary, starting from 0, and r is the right boundary, set to the last index of array A.

        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B 
        #i is the middle index of the current search range in array A, and j is calculated such that i and j together partition the arrays into two halves.

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

    #These lines set the boundary values for the partitions. If the index is outside the array, it uses -infinity for left boundaries and infinity for right boundaries.

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
    #This checks if the partitions are correct (i.e., the left side values are smaller than the right side values). If they are correct, it returns the median. If the total number of elements is odd, it returns the minimum of the right values. If even, it returns the average of the maximum left value and minimum right value.
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

    #If the partitions are not correct, these lines adjust the binary search boundaries for the next iteration.

# Time Complexity = O(log(min(n, m)))
