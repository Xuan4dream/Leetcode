#!/usr/bin/env python
# coding: utf-8

# In[6]:


# https://leetcode.com/problems/rectangle-area/
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A, B, C, D, E, F, G, H : int
        :rtype: int
        """
        # FIRST TRY 03192021
        area = (C-A)*(D-B) + (G-E)*(H-F)
        
        if (not ((A>=G) or (E>=C))) and (not (B>=H or (F>=D))):
            x_overlap = min(C, G) - max(A, E)
            y_overlap = min(D, H) - max(B, F)
            area = area - abs(x_overlap * y_overlap)
        
        return area
        ## Time: O(1)
        ## Space: O(1)
        
        # # Reference to the discussion 03192021
        # area = (C-A)*(D-B) + (G-E)*(H-F)
        # w = min(C,G)-max(A,E)
        # h = min(D, H)-max(B,F)
        # if w<=0 or h<=0:
        #     return area
        # else:
        #     return area - w*h

