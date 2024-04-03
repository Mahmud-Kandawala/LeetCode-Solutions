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

'''
Initial Setup
nums = [1, 2, 3, 4, 5], k = 2
window = set(), an empty set to track the elements in the current window.
L = 0, the start of the window.

Step-by-Step Execution

Iteration 1: R = 0
Current nums[R] = 1.
Check if R - L > k: 0 - 0 > 2 is False, so we skip the window adjustment.
Check if nums[R] in window: 1 is not in window, so we move to the next step.
Add nums[R] to window: window = {1}.

Iteration 2: R = 1
Current nums[R] = 2.
Check if R - L > k: 1 - 0 > 2 is False.
Check if nums[R] in window: 2 is not in window.
Add nums[R] to window: window = {1, 2}.

Iteration 3: R = 2
Current nums[R] = 3.
Check if R - L > k: 2 - 0 > 2 is False (it's equal, not greater).
Check if nums[R] in window: 3 is not in window.
Add nums[R] to window: window = {1, 2, 3}.

Iteration 4: R = 3 (Window Adjustment Starts)
Current nums[R] = 4.
Check if R - L > k: 3 - 0 > 2 is True. Now the window size is more than k, so we adjust it.
Remove nums[L] (1) from window: window = {2, 3}.
Increment L to 1.
Check if nums[R] in window: 4 is not in window.
Add nums[R] to window: window = {2, 3, 4}.

Iteration 5: R = 4 (Continuing Window Adjustment)
Current nums[R] = 5.
Check if R - L > k: 4 - 1 > 2 is True. Adjust the window again.
Remove nums[L] (2) from window: window = {3, 4}.
Increment L to 2.
Check if nums[R] in window: 5 is not in window.
Add nums[R] to window: window = {3, 4, 5}.

