class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        queue = deque()
        freq = {}

        for i,ch in enumerate(s):
            if ch not in freq:
                freq[ch] = 1
            else: 
                freq[ch] += 1
            
            queue.append((ch,i))

            while queue and freq[queue[0][0]] > 1:
                queue.popleft()

        return queue[0][1] if queue else -1

        