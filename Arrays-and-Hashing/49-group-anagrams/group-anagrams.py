class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        str_map = {}
        final_list = []
        #overall for loop for the given str list
        for word in strs: 
            #create a new empty freq list arr for each word 
            freq = [0] * 26
            #character position checker and tracker
            for ch in word: 
                freq[ord(ch) - ord('a')] += 1 
            key = tuple(freq)

            if key not in str_map: 
                str_map[key] = []
            str_map[key].append(word)
        final_list = list(str_map.values())
        return final_list
        