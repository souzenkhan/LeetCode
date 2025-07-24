from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # used python sorted method to sort the two strings and comparing them 
        # to return true or false
        return Counter(s) == Counter(t)
        

        