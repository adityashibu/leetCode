class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Define a variable to hold the number of consecutive odds
        count = 0
        
        # Loop until the end of the array
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                count = 0
            else:
                count += 1
            
            if count == 3:
                return True
        return False
            
        
