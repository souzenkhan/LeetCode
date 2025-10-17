class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #optimized solution 

        stack = []
        operators = {
            '+': lambda x, y:  x + y,
            '-': lambda x, y:  x - y,
            '*': lambda x, y:  x * y,
            '/': lambda x, y:  int(x /float(y))
        }


        for i in tokens: 
            if i in operators: 
                right = stack.pop()
                left = stack.pop()
                stack.append(operators[i](left, right))
            else: 
                stack.append(int(i))
                    
        return stack[-1]
        