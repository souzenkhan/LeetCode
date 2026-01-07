class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq_tracker = {}

        for letter in s:
            if letter in freq_tracker: 
                freq_tracker[letter] += 1
            else: 
                freq_tracker[letter] = 1

        for index, letter in enumerate(s): 
            if freq_tracker[letter] == 1:
                return index

        
        return -1

        


            



        