#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 04032021 SECOND TRY with reference to Approach 2
        counts = collections.Counter(nums)
        return max(counts.keys(), key = counts.get)
        # Time: O(N)
        # Space: O(N)
         
#         # 04032021 FIRST TRY
#         d = {}
#         majority_count = len(nums)//2
        
#         for num in nums:
#             if num in d:
#                 d[num] = d[num] + 1
#             else: 
#                 d[num] = 1
        
#         for k in d.keys():
#             if d[k] > majority_count:
#                 return k
#         # Time: O(N) 
#         # Space: O(N)

