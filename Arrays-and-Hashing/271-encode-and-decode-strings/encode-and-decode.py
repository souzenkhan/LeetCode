class Solution:

    def encode(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        encoded_str = ""
        for s in strs: 
            append_item = str(len(s)) + "#" + str(s)
            encoded_str += append_item
        return encoded_str


    def decode(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        decoded_strs = []
        i = 0 
        while i < len(s):
            j = i 
            #finding the position of the delimiter '#'
            while s[j] != "#":
                j += 1
            #extracting the length of the string and the string itself
            length = int(s[i:j])
            #moving the index past the delimiter
            i = j + 1 
            #appending the decoded string to the list
            decoded_strs.append(s[i:i+length])
            #updating the index to the next string
            i += length
        return decoded_strs

