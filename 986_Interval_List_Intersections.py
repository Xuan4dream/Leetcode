#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 986. Interval List Intersections

class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        # ANSWER 03122021
        ans = []
        i = j = 0
        
        while i < len(firstList) and j < len(secondList):
            # check if firstList[i] intersects secondList[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            
            if lo <= hi:
                ans.append([lo, hi])
            
            if firstList[i][1] < secondList[j][1]:
                i +=1
            else: 
                j +=1
        
        return ans

