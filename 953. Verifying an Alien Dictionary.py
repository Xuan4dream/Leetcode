#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # First try 04062021 reference to the solution        
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                # if there is no mismatch between words[i] and words[i+1]
                # we need to examine the case when words are like "apple", "app"
                if j >= len(words[i+1]): return False
                
                if words[i][j] != words[i+1][j]:
                    if order_index[words[i][j]] > order_index[words[i+1][j]]: 
                        return False
                    break            
        return True
    
#         ## Old code
#         word_count = len(words)
        
#         if word_count ==1:
#              return true
#         else: 
#             for i in range(word_count-1):
#                 word1 = words[i]
#                 word2 = words[i+1]
#                 if (word1[0:len(word2)] == word2) & (len(word1)> len(word2)):
#                     return False
#                 word12_min_len = min(len(word1), len(word2))
#                 for j in range(word12_min_len):
#                     if word1[j] != word2[j]:
#                         index1 = order.index(word1[j])
#                         index2 = order.index(word2[j])
#                         if index1 < index2:
#                             break
#                         else:
#                             return False

#         return True

