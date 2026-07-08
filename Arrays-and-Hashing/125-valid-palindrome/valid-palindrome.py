class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #tracking the left and right character for two pointer solution
        l = 0 
        r = len(s) - 1

        #left must always be lesser than right 
        while l < r: 
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            #if the left and right character don't match
            if s[l].lower() != s[r].lower():
                return False
            #after comparison, continue traversing 
            l += 1 
            r -= 1
        #if the while loop exits successfully 
        return True
        
