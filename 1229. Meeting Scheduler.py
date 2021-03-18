#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Solution(object):    
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        # FIRST TRY 03172021
        slots1 = [slot for slot in slots1 if (slot[1]-slot[0] >= duration)]
        slots2 = [slot for slot in slots2 if (slot[1]-slot[0] >= duration)]
        slots1.sort()
        slots2.sort()
        
        for slot1 in slots1:
            for slot2 in slots2:
                if not (slot1[0] >= slot2[1] or slot1[1] <= slot2[0]):
                    overlap = [max(slot1[0], slot2[0]), min(slot1[1], slot2[1])]
                    if overlap[1] - overlap[0] >= duration:
                        return [overlap[0], overlap[0] + duration]
        else: 
            return []
        ## Time: O(N*M) or O(NlogN) or O(MlogM)
        ## Space: O(N) or O(M)
        
#         # Reference code using two pointers
#         slots1.sort()
#         slots2.sort()
#         pointer1 = pointer2 = 0
        
#         while pointer1 < len(slots1) and pointer2 < len(slots2):
#             # find the overlap time if applicable
#             overlap_right = min(slots1[pointer1][1], slots2[pointer2][1])
#             overlap_left = max(slots1[pointer1][0], slots2[pointer2][0])
#             if overlap_right - overlap_left >= duration:
#                 return [overlap_left, overlap_left+duration]
#             # move the one ends earlier to the next
#             if slots1[pointer1][1] < slots2[pointer2][1]:
#                 pointer1 += 1
#             else: 
#                 pointer2 += 1
#         return [] 

#         ## Time: O(MlogM+NlogN)
#         ## Space: O(N) or O(M) 

