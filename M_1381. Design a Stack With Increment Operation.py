#!/usr/bin/env python
# coding: utf-8

# In[24]:


# 04162021
class CustomStack(object):
    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.l = []
        self.max_size = maxSize
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.l) < self.max_size:
            self.l.append(x)
        else:
            return -1
            print(self.l)
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.l) == 0:
            return -1
        else:
            return self.l.pop()
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if k <= len(self.l):
            for i in range(k):
                self.l[i] += val
        else:
            self.l = [x+val for x in self.l]
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

