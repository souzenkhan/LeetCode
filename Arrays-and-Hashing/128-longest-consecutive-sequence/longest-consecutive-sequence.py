class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if empty set is the input, simply return 0
        if not nums:
            return 0
        #create a set of the array
        num_set = set(nums)
        max_length = 0
        for x in num_set: 
            #start at the smallest potential value of a seq
            if x - 1 not in num_set: 
                current = x; 
                length = 1; 

                while current + 1 in num_set: 
                    current += 1
                    length += 1

                max_length = max(max_length, length)
        return max_length


        