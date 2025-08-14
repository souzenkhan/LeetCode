class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #using two pointer approach
        left = 0 
        right = len(s) -1 #due to index values

        #ensuring it is within range
        while left < right: 

            if s[left] == s[right]:
                left += 1
                right -= 1

            elif((s[left].isalpha() and s[right].isalpha()) and ((ord(s[left]) == ord(s[right]) + 32) or (ord(s[right]) == ord(s[left]) + 32))):
                left += 1
                right -=1 
            elif not (48 <= ord(s[left]) <= 57 or 65 <= ord(s[left]) <= 90 or 97 <= ord(s[left]) <= 122):
                left += 1
            elif not (48 <= ord(s[right]) <= 57 or 65 <= ord(s[right]) <= 90 or 97 <= ord(s[right]) <= 122):
                right -= 1
            #if the vals are within expected range and different then not a palindrome
            else: 
                return False
        #passes all conditions after checking with pointers
        return True
        