#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class MyCalendarTwo(object):

    def __init__(self):
        self.calendar = []
        self.overlap = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for s, e in self.overlap:
            if start < e and end > s:
                return False
        
        for s, e in self.calendar:
            if start < e and end > s:
                self.overlap.append([max(start, s), min(end, e)])
        
        self.calendar.append([start, end])
        return True

