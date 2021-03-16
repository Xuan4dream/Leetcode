#!/usr/bin/env python
# coding: utf-8

# In[6]:


## 1288. Remove Covered Intervals
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # THIRD TRY 03152021
        intervals.sort(key = lambda x: (x[0], x[0] - x[1]))
        n = len(intervals)
        output = n
        
        cur_max = intervals[0][1]
        for i in range(1, n):
            if intervals[i][1] <= cur_max:
                output -= 1
                # not update cur_max
            else:
                cur_max = intervals[i][1]
        return output
        ## Runtime: 72 ms, faster than 85.84% of Python online submissions for Remove Covered Intervals.
        ## Memory Usage: 14 MB, less than 36.28% of Python online submissions for Remove Covered Intervals.
        
#         # SECOND TRY 03152021
#         intervals.sort(key = lambda x: x[1] - x[0], reverse = True)
#         n = len(intervals)
        
#         covered = []
        
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
#                     covered.append(j)
        
#         covered = list(set(covered))
                    
#         return n - len(covered)        
#         ## Runtime: 1332 ms, faster than 5.31% of Python online submissions for Remove Covered Intervals.
#         ## Memory Usage: 28.7 MB, less than 6.19% of Python online submissions for Remove Covered Intervals.
    
#         # FIRST TRY 03142021
#         intervals.sort()
#         n = len(intervals)
#         covered = []
        
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if intervals[i][0] == intervals[j][0] and intervals[j][1] >= intervals[i][1]:
#                     covered.append(i)  
#                 elif intervals[i][0] < intervals[j][0] and intervals[i][1] >= intervals[j][1]:
#                     covered.append(j)
        
#         covered = list(set(covered))
                    
#         return n - len(covered)
        
#         ## Runtime: 1856 ms, faster than 5.31% of Python online submissions for Remove Covered Intervals.
#         ## Memory Usage: 28.6 MB, less than 6.19% of Python online submissions for Remove Covered Intervals.

