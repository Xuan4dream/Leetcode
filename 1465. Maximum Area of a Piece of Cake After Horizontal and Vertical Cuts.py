#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        # 04122021 First try
        
        def get_diff(input_list, max_value):
            input_list.append(0)
            input_list.append(max_value)
            input_list.sort()
            
            output = []
            for i in range(1, len(input_list)):
                output.append(input_list[i] - input_list[i-1])
            return output
        
        return max(get_diff(horizontalCuts, h))*max(get_diff(verticalCuts, w))%(10**9+7)
        
        # Time: O(Nlog(N))
        # Space: O(N)

