class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {")" : "(", "}" : "{", "]" : "["}

        for bracket in s: 
            if bracket in "({[":
                stack.append(bracket)
            else: 
                if not stack or stack[-1] != pairs[bracket]:
                    return False
                stack.pop()

        return not stack

        