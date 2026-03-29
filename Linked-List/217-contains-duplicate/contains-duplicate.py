class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        tracker = {}
        for i in nums: 
            if i not in tracker: 
                tracker [i] = 1
            else: 
                return True
        return False
        
        