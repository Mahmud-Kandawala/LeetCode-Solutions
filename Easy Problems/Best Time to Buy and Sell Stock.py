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



