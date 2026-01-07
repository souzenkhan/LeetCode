class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_check = {}

        for x,i in enumerate(nums):
            difference = target - i

            if difference in num_check: 
                return [num_check[difference], x]

            num_check[i] = x

        