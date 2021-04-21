#!/usr/bin/env python
# coding: utf-8

# In[24]:


class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a == 1:
            return a
        
        i = 9
        output = []
        while i > 1:
            if a%i == 0:
                a = a/i
                output.append(i) 
                if a == 1:
                    break
            else:
                i -=1
        
        n = len(output)
        if n == 0 or a != 1:
            return 0
        
        result = 0
        for i in range(n):
            result = result + output[i]*10**(i)
        
        if result <2**31-1:
            return result
        else:
            return 0
    
    # Time: O(8loga)
    # Space: O(loga)

