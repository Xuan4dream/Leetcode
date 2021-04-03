#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 04032021 Second try referencing the Boyer-Moore Voting Algorithm
        
        # 1st pass
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        
        for n in nums:
            if candidate1 == n:
                count1 +=1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
                
        # 2nd pass
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums)//3:
                result.append(c)
        
        return result
        # Time: O(N)
        # Space: O(1)
        
        # # 04032021 First try
        # counts = collections.Counter(nums)
        # return [k for k in counts if counts[k] > len(nums)//3]
        # # Time: O(N)
        # # Space: O(N)

