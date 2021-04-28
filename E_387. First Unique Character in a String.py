#!/usr/bin/env python
# coding: utf-8

# In[44]:


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """    
        # solution 
        # build hash map: character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1

        
#         # 04272021 First try
#         d = {}
        
#         for i in range(len(s)):
#             letter = s[i]
#             if letter in d:
#                 d[letter].append(i)
#             else:
#                 d[letter] = [i]
        
#         unique = [d[letter] for letter in d if len(d[letter]) == 1]
#         # print(unique)
        
#         if len(unique) == 0:
#             return -1
#         else:
#             return min(unique)[0]
        
#         # Time: O(N)
#         # Space: O(1)

#         # second try
#         count = collections.Counter(s)
#         unique = []
        
#         for ch in count:
#             if count[ch] == 1:
#                 unique.append(ch)
        
#         if len(unique) == 0:
#             return -1
        
#         min_index = len(s) + 1
        
#         for ch in unique:
#             min_index = min(min_index, s.index(ch))
            
#         return min_index

