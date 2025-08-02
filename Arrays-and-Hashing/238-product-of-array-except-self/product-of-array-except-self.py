class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prefix_arr = []
        suffix_arr = [1] * len(nums)
        prefix_prod_track = 1
        suffix_prod_track = 1

        #prefix array
        for i in range(len(nums)):
            prefix_arr.append(prefix_prod_track)
            prefix_prod_track *= nums[i]

        #suffix array
        for i in range(len(nums) - 1, -1, -1):
            suffix_arr[i] = suffix_prod_track
            suffix_prod_track *= nums[i]

        output_arr = []
        #output array multiplied at the index vals
        #of prefix and suffix array
        for i in range(len(nums)):
            output_arr.append(prefix_arr[i]*suffix_arr[i])
        return output_arr        