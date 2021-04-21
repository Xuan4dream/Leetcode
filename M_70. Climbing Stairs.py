#!/usr/bin/env python
# coding: utf-8

# In[24]:


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 04212021 first try
        steps = [0, 1, 2]
        
        for i in range(3, n+1):
            steps.append(steps[i-1] + steps[i-2])
        
        return steps[n]
    
    # Time: O(N)
    # Space: O(N)

