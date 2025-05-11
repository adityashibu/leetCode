# Start off by checking if the current number - 1 exists in the set
# If it does then that means the current number is not the start of a set, if it doesn't then the current number is the start of a set
# Now continue by checking if the current number + 1 is in the set, in which case increment the counter you made to keep track of length, by 1

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for i in numSet:
            # Check if the current number is the start of a sequence
            if (i - 1) not in numSet:
                length = 0

                # As you increment length by 1, it checks the current number + length, basically if i was 1, it would check 1 + 1 = 2, 1 + 2 = 3, 1 + 3 = 4
                while (i + length) in numSet:
                    length += 1

                longest = max(longest, length)

        return longest 