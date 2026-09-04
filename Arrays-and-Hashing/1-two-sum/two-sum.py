class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        tracker = {}

        for x, i in enumerate(nums):
            difference = target - i 
            if difference in tracker: 
                return [x, tracker[difference]]
            else: 
                tracker[i] = x