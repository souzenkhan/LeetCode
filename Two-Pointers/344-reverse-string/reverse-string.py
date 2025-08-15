class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        s_copy = s[:]
        print(s_copy)

        for i,x in enumerate(s):
            last = s_copy.pop()
            print(last)
            s[i] = last









       

        





        