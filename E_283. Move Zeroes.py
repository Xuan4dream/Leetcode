#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        for i in range(n):
            if nums[n-1-i]==0:
                nums.pop(n-1-i)
                nums.append(0) 

