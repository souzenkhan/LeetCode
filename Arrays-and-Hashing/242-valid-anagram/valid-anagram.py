class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # used python sorted method to sort the two strings and comparing them 
        # to return true or false
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        
        if s_sorted == t_sorted: 
            return True
        return False
        