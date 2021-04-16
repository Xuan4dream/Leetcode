#!/usr/bin/env python
# coding: utf-8

# In[24]:


# 04152021 
class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.l = [0]*length
        self.snapshots = []
        self.id = -1  # index
        self.d = {}   # dict to store the changed value in set()

        
    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.l[index] = val
        self.d[index] = val

    def snap(self):
        """
        :rtype: int
        """
        self.id += 1
        # need to make a copy since if directly append, 
        # since it will change when self.l being updated
        d_copy = dict(self.d) 
        self.snapshots.append(d_copy)
        return self.id
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        if index not in self.snapshots[snap_id]:
            return 0
        else:
            return self.snapshots[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

