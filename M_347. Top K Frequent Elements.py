#!/usr/bin/env python
# coding: utf-8

# In[24]:


import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.Counter(nums)
        
        l = [[num, d[num]] for num in d]
        
        l.sort(key = lambda x: x[1], reverse = True)
        
        l = [num for num, count in l[:k]]
        
        return l

