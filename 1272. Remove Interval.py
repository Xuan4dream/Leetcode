#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 1272. Remove Interval Medium
class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        # SECOND TRY using solution 03152021
        remove_start, remove_end = toBeRemoved
        ans = []
        
        for start, end in intervals:
            # if no overlap --> add the interval to ans
            if start >= remove_end or end <= remove_start:
                ans.append([start, end])
            else: 
                if start < remove_start:
                    ans.append([start, remove_start])
                if end > remove_end:
                    ans.append([remove_end, end])
        
        return ans
        ## Runtime: 316 ms, faster than 80.65% of Python online submissions for Remove Interval.
        ## Memory Usage: 20.7 MB, less than 14.52% of Python online submissions for Remove Interval.
        
               
        # FIRST TRY 03152021
        # initial setup
        remove_start, remove_end = toBeRemoved
        idx, n = 0, len(intervals)
        ans = []
        
        # interval starts before toBeRemoved
        while idx < n and remove_start >= intervals[idx][1]:
            ans.append(intervals[idx])
            idx +=1
        
        # overlap scenarios
        while (idx < n) and (intervals[idx][0]< remove_end): 
            # inter_start, inter_end = intervals[idx]
            if intervals[idx][0] < remove_start:
                if remove_start <= intervals[idx][1] <= remove_end:
                    ans.append([intervals[idx][0], remove_start])
                else: 
                    ans.append([intervals[idx][0], remove_start])
                    ans.append([remove_end, intervals[idx][1]])
            elif (remove_start<= intervals[idx][0]) and intervals[idx][1] > remove_end:
                ans.append([remove_end, intervals[idx][1]])
            idx +=1
            
        # after cases:
        while idx < n:
            ans.append(intervals[idx])
            idx +=1
            
        return ans
    
    ## Runtime: 316 ms, faster than 80.65% of Python online submissions for Remove Interval.
    ## Memory Usage: 19.3 MB, less than 100.00% of Python online submissions for Remove Interval.

