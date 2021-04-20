#!/usr/bin/env python
# coding: utf-8

# In[24]:


# 04192021
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.l = nums
        # calculate the prefix sum for each index
        self.l_cum_sum = []
        s = 0
        for i in range(len(nums)):
            s = s + nums[i]
            self.l_cum_sum.append(s)

            
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return(self.l_cum_sum[right])
        else:
            return(self.l_cum_sum[right] - self.l_cum_sum[left-1])
        
        # Time: O(N) for initialization, O(1) for sumRange
        # Space: O(N) 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

