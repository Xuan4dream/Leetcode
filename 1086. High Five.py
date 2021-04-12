#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """     
        # First try 04112021
        d = {}
        
        for student, score in items:
            if student in d:
                d[student].append(score)
            else:
                d[student] = [score]
        
        output = []
        
        for student in d:
            scores = d[student]
            d[student].sort(reverse = True)
            avg_score = sum(scores[0:5])/5
            output.append([student, avg_score])
        
        output.sort()
        
        return output

