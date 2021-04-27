#!/usr/bin/env python
# coding: utf-8

# In[44]:


class Solution(object):    
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # refered to solution:
        # 0- north, 1- east, 2-south, 3-west
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # inital position 
        x = y = 0
        # facing north
        idx = 0
        
        for i in instructions:
            if i == "L":
                idx = (idx +3)%4
            elif i == "R":
                idx = (idx +1)%4
            else:
                x += directions[idx][0]
                y += directions[idx][1]
        
        # after one circle: it returns to the inital position
        # or doesn't face north, then it is bounded
        return (x == 0 and y == 0) or idx != 0
        
#         # 04262021 First try with hints
#         self.loc = [0, 0]
#         self.direction = [0, 1]
        
#         for ins in instructions:
#             self.move(ins)
        
#         if self.direction != [0, 1] or self.loc == [0, 0]:
#             return True
#         else:
#             return False
        
#     def move(self, ins):
#         left_dir  = [[0, 1], [-1, 0], [0, -1], [1, 0], [0, 1]]
#         right_dir = [[0, 1],  [1, 0], [0, -1], [-1, 0], [0, 1]]
        
#         if ins == "G":
#             self.loc = [self.loc[i]+self.direction[i] for i in (0, 1)]
#         elif ins == "L":
#             self.direction = left_dir[left_dir.index(self.direction) + 1]
#         else:
#             self.direction = right_dir[right_dir.index(self.direction) + 1]
    
#     # Time: O(N)
#     # Space: O(1)

