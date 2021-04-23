#!/usr/bin/env python
# coding: utf-8

# In[44]:


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """                       
        # referred to Discussion StefanPochmann
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller
        
#         # 04222021 first try|Binary Search|Time limit exceeded 
#         n = len(nums)
#         res = [0]*n
        
#         if max(nums) == min(nums):
#             return res
        
#         d = collections.Counter(nums)
#         num_count = [[num, d[num]] for num in d]
#         num_count.sort()
#         n_num = len(num_count)
        
#         for i in range(n):
#             num = nums[i]
#             left, right = 0, n_num-1
            
#             while left <= right:         
#                 mid = (left + right)//2
#                 if num_count[mid][0] > num:
#                     right = mid-1
#                 elif num_count[mid][0] < num:
#                     left = mid+1
#                 else: 
#                     break
#             count = [i for num, i in num_count[:mid]]
#             res.append(sum(count))
#             num_count[mid][1] =  num_count[mid][1] - 1
            
#         return res
#       # stopped at 48 / 65

#         ## second try Time limit exceeded
#         n = len(nums)
#         res = [0] * n
#         index_num = list(enumerate(nums))
#         index_num.sort(key = lambda x: x[1])
#         sorted_index = [i for i, num in index_num]
#         sorted_num = [num for i, num in index_num]
                         
#         for i in range(n):
#             num = nums[i]
#             first_index = sorted_num.index(num)
#             count = [1 if j > i else 0 for j in sorted_index[:first_index]]
#             res[i] = sum(count)
        
#         return res
#     # Stopped at 14/65

