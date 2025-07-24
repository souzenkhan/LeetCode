class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #creating a dictionary to store the numbers and their occurrences
        nums_dict = {}
        #iterating through the list to check for duplicate occurences
        for i in nums: 
            if i in nums_dict:
                #if a number exists in the dictionary return True
                return True
            else: 
                #otherwise add the number to the dictionary
                nums_dict[i] = 1
            #if duplicates are not found, return False
        return False





        