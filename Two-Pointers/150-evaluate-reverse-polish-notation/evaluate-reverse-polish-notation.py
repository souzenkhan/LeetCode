class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        def calc(left, right, op):
            result = 0
            if op == '+': return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/': return int(left / float(right))


        stack = []


        for i in tokens: 
            try: 
                stack.append(int(i))
            except ValueError: 
                right = stack.pop()
                left = stack.pop()
                stack.append(calc(left, right, i))
                    
        return stack[-1]
        