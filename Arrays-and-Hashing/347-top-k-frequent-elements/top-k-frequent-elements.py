class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #initialize a dictionary to store frequencies
        freq_map = defaultdict(int)

        #for loop to increment frequencies with corresponding vals
        for num in nums: 
            freq_map[num] += 1
        
        #create empty buckets for appropriate range
        buckets = [[] for _ in range(len(nums) + 1)]

        #taking the number and the frequency append the 
        #number at the corresponding freq index
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        result = []
        #check starting backwards
        for i in range(len(buckets) - 1, -1, -1):
            #for values in the buckets, append to result 
            #highest freq (since we started from the back)
            #is appended to result 
            for num in buckets[i]:
                result.append(num)
                #return result as soon as it reaches the length specified, k
                if len(result) == k:
                    return result
        