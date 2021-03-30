#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """      
        # 03292021 FIRST TRY with reference from the discussion     
        # arr = [s for s in arr if len(arr) == len(set(arr))]
        
        unique_list = [""]
        max_len = 0
        
        for s in arr:
            for unique in unique_list:
                new_unique = s + unique
                if len(new_unique) == len(set(new_unique)):
                    unique_list.append(new_unique)
                    max_len = max(max_len, len(new_unique))
        
        print(unique_list)
        return max_len

