#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # one pass
        # minprice = float("inf")
        minprice = prices[0]
        maxprofit = 0
        
        for i in range(1, len(prices)):
            # update global minmal
            if prices[i] < minprice:
                minprice = prices[i]
            # update global maxprofit
            if prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit
        
        
#         # 03262021 SECOND TRY
#         if len(prices) <=1:
#              return 0
        
#         increase = [(prices[i] - prices[i-1]) for i in range(1,len(prices))]
        
#         curr_profit = max_profit = increase[0]
        
#         for i in range(1, len(increase)):
#             curr_profit = max(curr_profit + increase[i], increase[i])
#             max_profit = max(max_profit, curr_profit)
            
#         if max_profit >0:
#             return max_profit
#         else:
#             return 0

