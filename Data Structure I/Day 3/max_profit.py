"""
Task
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 104

"""

from typing import List, Tuple
from sys import maxsize

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit variable
        max_profit: int = 0
        # minimum price varible to hold minimum price at j in price[j]
        minimum_price: int = maxsize
        # iterate through list
        for price in prices:
            # if the current price is lower than our minimum
            if minimum_price > price:
                # set that price to our minimum
                minimum_price = price
            # the max profit compares the current max_profit and the profit made between the current stock price and minimum price
            max_profit: int = max(max_profit, price - minimum_price)
        return max_profit

Solution().maxProfit(prices = [7,1,5,3,6,4])
Solution().maxProfit(prices = [7,6,4,3,1])
Solution().maxProfit(prices = [2,4,1])
Solution().maxProfit(prices = [2,1,2,1,0,1,2])
Solution().maxProfit(prices = [3,3,5,0,0,3,1,4])

