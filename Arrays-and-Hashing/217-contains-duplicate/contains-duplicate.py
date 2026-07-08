class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        appears = set()

        for i in nums:
            if i not in appears:
                appears.add(i)
            elif i in appears: 
                return True 
        return False