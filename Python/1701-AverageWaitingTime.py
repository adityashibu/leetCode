class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # Keep track of last completed order time
        t = 0
        # Total wait time for all customers
        total = 0
        
        for x, y in customers:
            # If arrival time is greater than last completed order time t, then update t to x
            t = max(x, t)
            
            # Calculate new wait time for the current customer
            total += t - x + y
            # Update the last completed order time
            t += y
            
        # Return the average
        return total / len(customers)