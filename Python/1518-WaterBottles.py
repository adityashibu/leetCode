class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Keep a track of all bottles you've drank
        totalCount = numBottles
        
        while numBottles >= numExchange:
            # Calculate the quotient to know how many full bottles can be obtained
            quotient = numBottles // numExchange
            # Calculate the remainder to know how many empty bottles can be obtained 
            remainder = numBottles % numExchange
           
            # Add the calculated full bottles to the totalCount
            totalCount += quotient
            
            # Calculate the new numBottles 
            numBottles = quotient + remainder
        # Finally return the total number of bottles drank
        return totalCount
            
            