#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 03272021 SECOND TRY
        res = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        
        return res
        
        
#         # 03272021 FIRST TRY
#         if len(prices) <= 1:
#             return 0
        
#         increase = [prices[i] - prices[i-1] for i in range(1, len(prices))]
#         increase = [i for i in increase if i > 0]
        
#         return sum(increase)

