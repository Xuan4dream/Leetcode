#!/usr/bin/env python
# coding: utf-8

# In[81]:


from random import choice
class RandomizedSet(object):
# 04122021 First try referring to the solution
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list =[]
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        else:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            # move the last element to the place idx of the val which will be deleted
            last_element = self.list[-1]
            idx = self.dict[val]
            self.list[idx] = last_element
            self.dict[last_element] = idx
            # delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        else:
            return False
        
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return choice(self.list)
        
    # Time: O(1)
    # Space: O(N)
    # From chaaloftin: if you remove an element that is not at the last index within a list, 
    # you will have to "shift" every element to the right of it to the left.

