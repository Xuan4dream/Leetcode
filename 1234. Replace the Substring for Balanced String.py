#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = n = len(s)
        count = collections.Counter(s)
        # this returns a dictionary of QWER as key and count as value
        
        i = 0
        for j, char in enumerate(s):
            count[char] -= 1
            while i < n and all(n / 4 >= count[c] for c in 'QWER'):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res
        ## Time complexity: O(N)

