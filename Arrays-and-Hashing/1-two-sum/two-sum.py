class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        traversed = {}

        for i,x in enumerate(nums):
            y = target - x
            if y in traversed: 
                return [traversed[y], i]
            else:
                traversed[x] = i

        