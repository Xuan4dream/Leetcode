#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 57. Insert Interval
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # SECOND TRY 03132021
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []
        
        # add all intervals before newInterval
        while idx<n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx +=1
        
        # add newInterval
        # if no overlap, then add the interval
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        # if there is an overlap, merge with the last interval
        else: 
            output[-1][1] = max(output[-1][1], new_end)
            
        # add the remaining intervals, merge with newInterval if needed
        while idx < n:
            start, end = intervals[idx]
            # if no overlap, just add an interval
            if output[-1][1] < start:
                output.append(intervals[idx])
            # if with overlap, merge with the last element in the output
            else: 
                output[-1][1] = max(output[-1][1], end)
            idx += 1
            
        return output
    
        
#         # FIRST TRY 03132021
                
#         intervals.append(newInterval)
#         intervals.sort()
        
#         ans = [intervals[0]]
        
#         for i in range(1, len(intervals)):
#             if ans[-1][1] < intervals[i][0]:
#                 ans.append(intervals[i])
#             else:
#                 ans[-1][1] = max(ans[-1][1], intervals[i][1])
                
#         return ans

