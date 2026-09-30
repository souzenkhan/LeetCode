class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
       #we use a set to track the items , so recurring vals dont cause confusion
        num_set = set(nums)
        longest_streak = 0 
        for i in num_set: 
            if i - 1 not in num_set: 
                current_streak = 1
                current_num = i 

                while (current_num + 1) in num_set: 
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
