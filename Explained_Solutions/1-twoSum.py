# Using a hashmap, we can keep track of already seen elements from the set. Mapping the value to its index
# Then we can keep checking if the target - current number has been seen in the hashmap as this would give the second number that needs to be found
# Once you find the second number, return the index of the two numbers

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # Value : Index

        # For each index and number in the enumeration of numbers
        for i, n in enumerate(nums):
            # Find the complement, which would be the second number you need to find
            complement = target - n

            # If the second number was already seen then
            if complement in seen:
                # Return the index of the second number, along with index of the current number
                return [seen[complement], i]
            
            # Else add the current number to the hashmap along with its index
            seen[n] = i