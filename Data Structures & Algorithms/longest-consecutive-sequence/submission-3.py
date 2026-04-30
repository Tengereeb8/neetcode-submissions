class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Convert to a set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # 2. Check if this is the START of a sequence
            # (If num - 1 is in the set, 'num' is not the start)
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # 3. Count how long this sequence goes
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                # 4. Update the global maximum
                longest_streak = max(longest_streak, current_streak)

        return longest_streak