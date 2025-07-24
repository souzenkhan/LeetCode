class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}
        occurences = []
        for i in nums: 
            if i in nums_dict:
                return True
            else: 
                nums_dict[i] = 1
        return False





        