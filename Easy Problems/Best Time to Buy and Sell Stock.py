class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #Left buy (Day 1), Right sell (Day 2)
        maxP = 0 #Keep track of the maximum profit observed

        while r < len(prices): #Loop iterates through 'prices'. Checks that r is within the bounds
            if prices[l] < prices[r]: #If the price on day l is less than the price on day r
                profit = prices[r] - prices [l]
                maxP = max(maxP, profit)
            else:
                l = r #Updates the l pointer to the current position of r because it would be better to consider buying at a lower price
            r += 1 #Pointer is incremented to consider the next day as a potential day to sell the stock
        
        return maxP #Returns the maximum profit 


#Example: [7, 1, 5, 3, 6, 4]
"""
Step 1: Initialization
Input: [7, 1, 5, 3, 6, 4]
Pointers: l = 0, r = 1
Maximum Profit: maxP = 0

Step 2: First Iteration
Check: prices[l] = 7 vs. prices[r] = 1
Since 7 > 1, we set l = r = 1.
Move to the next iteration by incrementing r to 2.

Step 3: Second Iteration
Check: prices[l] = 1 vs. prices[r] = 5
Since 1 < 5, the profit would be 5 - 1 = 4.
Update maxP to 4 since it's greater than the current value 0.
Increment r to 3.

Step 4: Third Iteration
Check: prices[l] = 1 vs. prices[r] = 3
Since 1 < 3, the profit would be 3 - 1 = 2.
maxP remains 4 since 2 is less than 4.
Increment r to 4.

Step 5: Fourth Iteration
Check: prices[l] = 1 vs. prices[r] = 6
Since 1 < 6, the profit would be 6 - 1 = 5.
Update maxP to 5 since it's greater than the current value 4.
Increment r to 5.

Step 6: Fifth Iteration
Check: prices[l] = 1 vs. prices[r] = 4
Since 1 < 4, the profit would be 4 - 1 = 3.
maxP remains 5 since 3 is less than 5.
Increment r to 6, which ends the loop since r is now out of bounds.
"""
