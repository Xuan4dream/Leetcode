#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # SECOND TRY 03172021
        if not points:
            return 0
        
        points.sort()
        overlap = points[0]
        count = 1
        
        for point in points[1:]:
            if (overlap[0] > point[1]) or (overlap[1] < point[0]):
                overlap = point
                count += 1
            else: 
                overlap = [point[0], min(overlap[1], point[1])]
        
        return count
    ## Time: O(NlogN)
    ## Space: O(N) 
    ## the list.sort() function in Python is implemented with the Timsort algorithm whose space complexity is O(N).
        
#         # FIRST TRY 03172021
#         n = len(points)
#         if n == 0:
#             return 0
        
#         points.sort()
        
#         overlaps =[points[0]]
        
#         for point in points[1:]:
#             prev_start, prev_end = overlaps[-1]
#             curr_start, curr_end = point
#             if (prev_start > curr_end) or (prev_end < curr_start):
#                 overlaps.append(point)
#             else: 
#                 overlaps[-1] = [max(prev_start, curr_start), min(prev_end, curr_end)]
        
#         return len(overlaps)
    
#     ## Runtime: 388 ms, faster than 33.55% of Python online submissions for Minimum Number of Arrows to Burst Balloons.
#     ## Memory Usage: 19 MB, less than 61.94% of Python online submissions for Minimum Number of Arrows to Burst Balloons.
        

