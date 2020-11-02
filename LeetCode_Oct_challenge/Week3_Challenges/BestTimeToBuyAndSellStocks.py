'''
You are given an integer array prices where prices[i] is the price of
a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete
at most k transactions.

Notice that you may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
'''


class Solution:
    def maxProfit(self, k: int, prices) -> int:
        if 2*k >= len(prices):
            return sum(max(0, prices[i]-prices[i-1]) for i in range(1, len(prices)))
        res = [0]*len(prices)
        for _ in range(k):
            val = 0
            for i in range(1, len(res)):
                val = max(res[i], val + prices[i] - prices[i-1])
                res[i] = max(res[i-1], val)
        return res[-1]


obj = Solution()
res = obj.maxProfit(2, [2, 4, 1])
print(res)
