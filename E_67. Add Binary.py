#!/usr/bin/env python
# coding: utf-8

# In[44]:


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 04292021 Bit-by-Bit Computation solution 
        n = max(len(a), len(b))
        
        a, b = a.zfill(n), b.zfill(n)
        
        carry = 0 
        answer = []
        
        for i in range(n-1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1
                
            if carry %2 == 1:
                answer.append("1")
            else: 
                answer.append("0")
            
            carry //= 2
            
        if carry == 1:
            answer.append("1")
        
        answer.reverse()
        
        return "".join(answer)
        # Time: O(max(N, M))
        # Space: O(max(N, M))

