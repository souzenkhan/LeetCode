class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        str_stack = []

        for i in s: 
            if(i == '(' or i == '{' or i == '['):
                str_stack.append(i)
            elif(i == ')' or i == '}' or i == ']'):
                #if there is no other info on the stack and there is a closing bracket return False
                if(bool(str_stack) == False):
                    return False

                last = str_stack.pop()
                if(i==')'):
                    if (last == '('):
                        continue
                    else: 
                        return False
                elif(i=='}'):
                    if (last == '{'):
                        continue
                    else: 
                        return False
                elif(i==']'):
                    if (last == '['):
                        continue
                    else: 
                        return False
        isEmpty = not bool(str_stack)
        if(isEmpty):
            return True
        else: 
            return False
                
        