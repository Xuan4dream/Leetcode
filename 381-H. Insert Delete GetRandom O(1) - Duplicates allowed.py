#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 04132021 First try referring to the solution
import random
class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.idx = defaultdict(set)

        
    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not  contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.idx[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.idx[val]) == 1
            
        
    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.idx[val]:
            return False
        remove, last = self.idx[val].pop(), self.lst[-1]
        self.lst[remove] = last
        self.idx[last].add(remove)
        self.idx[last].discard(len(self.lst) - 1)
        # discard() removes the element from the set only if the element is present in the set. 
        # If it is not present in the set, then no error or exception is raised and the original set is printed.
        
        self.lst.pop()
        return True
            

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.lst)
    
# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

