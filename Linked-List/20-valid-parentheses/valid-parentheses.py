class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {")" : "(", "}" : "{", "]" : "["}

        for i in s: 
            if i in "({[":
                stack.append(i)

            else: 
                if not stack or stack[-1] != pairs[i]:
                    return False
                stack.pop()

        return not stack