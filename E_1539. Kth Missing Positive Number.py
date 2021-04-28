#!/usr/bin/env python
# coding: utf-8

# In[44]:


class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # solution 2 binary search
        left, right = 0, len(arr) -1
        while left <= right:
            pivot = (left+right)//2
            # If number of positive integers which are missing before arr[pivot]
            # is less than k --> continue to search on the right.
            if arr[pivot] - (pivot + 1) < k:
                left = pivot + 1
            # Otherwise, go left
            else:
                right = pivot - 1
        
        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 --> the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k

#         # solution 1
#         if k <= arr[0] - 1:
#             return k
#         k -= arr[0] - 1

#         # search kth missing between the array numbers
#         for i in range(len(arr) - 1):
#             # missing between arr[i] and arr[i + 1]
#             curr_missing = arr[i + 1] - arr[i] - 1
#             # if the kth missing is between arr[i] and arr[i + 1] -> return it
#             if k <= curr_missing:
#                 return arr[i] + k
#             # otherwise, proceed further
#             k -= curr_missing

#         # if the missing number if greater than arr[-1]
#         return arr[-1] + k        
               
    
#         # 04272021 Second try
#         m = arr[-1]
#         res = 0
#         for i in range(1, m):
#             if i not in arr:
#                 k -= 1
#                 res = i
#                 if k == 0:
#                     return res
#         return m + k
        
        
#         # 04272021 First try
#         m = arr[-1]
#         missing = []
        
#         for i in range(1, m):
#             if (i in arr) == False:
#                 missing.append(i)
            
#         # n = len(missing)
        
#         if len(missing) >= k:
#             return missing[k-1]
#         else:
#             return k-len(missing)+m
#         # Time: O(M) - M is the biggest value 
#         # Space: O(N) - N is the count of the missing values in the arr

