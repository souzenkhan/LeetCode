class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for s in strs: 
            count = [0] * 26

            for ch in s: 
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)

            if key not in groups: 
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())
        