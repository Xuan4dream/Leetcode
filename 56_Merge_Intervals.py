#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n <= 1:
            return intervals
        
        intervals.sort()   # inplace sort
        output = [intervals[0]]
        
        for i in range(1, len(intervals)):
            new_start = intervals[i][0]
            old_end = output[-1][1]
            if new_start <= old_end:   # with overlap
                new_interval = [output[-1][0], max(old_end, intervals[i][1])]
                output[-1] = new_interval
            else:
                output.append(intervals[i])
        
        return output

