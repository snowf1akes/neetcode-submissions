class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        L = 0 #buy
        R = 1 #sell
        while R in range(len(prices)):
            if prices[L] < prices[R]: #conditions when profit exists
                profit = prices[R] - prices[L]
                maxProf = max(profit, maxProf) 
            else: #if its negative, move left pointer forward
                L = R
            R += 1 #happens regardless of conditions 


        return maxProf