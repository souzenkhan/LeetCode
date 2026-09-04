class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tracker = set()
        for i in nums: 
            if i not in tracker: 
                tracker.add(i)
            elif i in tracker:  
                return True
        return False

        