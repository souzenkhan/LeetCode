class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        res = [0] * len(temperatures)
        stack = [] #will store temp, index pairs

        for i, t in enumerate(temperatures):
            while (stack and t > stack[-1][0]):
                stackTemp, stackIndex = stack.pop() 
                res[stackIndex] = (i - stackIndex)
            stack.append([t, i])
        return res