class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hashmap to store all previous elements
        prevMap = {}
        
        # Iterate through the items in the list, by taking the index as well as the number itself n
        for i, n in enumerate(nums):
            # Get the diff, which is number subtracted from the target
            diff = target - n
            # If the difference is in the hashmap then return a list with the index of that number with the index of the number that added to the target
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            
        # Since we know there is always going to be a solution, we can just return back in this case
        return