class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set() #Used to store the unique elements from nums that are within the current window of size k
        L = 0

        for R in range(len(nums)):
            if R - L > k: #Checks if the current window size is greater than k. If it is, it means we need to shrink the window from the left
                window.remove(nums[L]) # removes the leftmost element from window because it's no longer within the distance k from the current element
                L += 1 # increments L, effectively moving the left boundary of the window to the right.
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False #If the method completes the loop without finding any duplicates within the specified distance, it returns False
