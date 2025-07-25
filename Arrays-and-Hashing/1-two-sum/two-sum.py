class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_check = {}

        for x, i in enumerate(nums): 
            # find difference such that i + difference = target
            difference = target - i
            #if that difference exists in the dictionary, 
            #return the indices of both
            if difference in nums_check: 
                return [nums_check[difference], x]
            #otherwise it appends the index with the value 
            #to the dictionary
            nums_check[i] = x

            

            

        