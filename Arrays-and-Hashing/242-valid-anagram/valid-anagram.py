from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # using counter to count the frequency of characters in both strings
        # returns the comparison 
        return Counter(s) == Counter(t)
        

        