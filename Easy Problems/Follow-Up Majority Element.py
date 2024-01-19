# Majority Element LeetCode Follow-Up Question:
# Follow-up: Could you solve the problem in linear time and in O(1) space?

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result, count = 0, 0 #Two variables are initialized. result will eventually hold the majority element, and count is used to track the frequency of a potential majority element.
        for n in nums: #This loop iterates through each element (n) in the array nums.
             if count == 0: ## If count is 0, it means one of two things: This is the first element of the array, or The previous elements have effectively canceled each other out (none was dominant). In either case, the current element n is a new candidate for the majority element, so it's assigned to result. 
                 result = n
             count += (1 if n == result else -1)  #This line updates the count: If n is the same as the current result, count is incremented by 1 (since we found another instance of the potential majority element). If n is different from result, count is decremented by 1 (indicating that this element is not the same as our current candidate, reducing its likelihood of being the majority).
        return result


'''
Initialization: [3, 3, 4, 2, 4, 4, 2, 4, 4]

result and count are initialized to 0.

First Iteration (n = 3):
count is 0, so result becomes 3.
count is incremented to 1 since n is equal to result.

Second Iteration (n = 3):
count is not 0, so no change to result.
count is incremented to 2, as n (3) is equal to result (3).

Third Iteration (n = 4):
count is decremented to 1, as n (4) is not equal to result (3).

Fourth Iteration (n = 2):
count is decremented to 0, as n (2) is not equal to result (3).

Fifth Iteration (n = 4):
count is 0, so result becomes 4.
count is incremented to 1.

Sixth Iteration (n = 4):
count is incremented to 2, as n (4) is equal to result (4).

Seventh Iteration (n = 2):
count is decremented to 1, as n (2) is not equal to result (4).

Eighth Iteration (n = 4):
count is incremented to 2, as n (4) is equal to result (4).

Ninth Iteration (n = 4):
count is incremented to 3, as n (4) is equal to result (4).

End of Loop:
The function returns result, which is 4.
'''
