class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Define a queue to simulate the cycle
        queue = []
        
        # Push the elements into the queue
        for i in range(1, n + 1):
            queue.append(i)
            
        # While there are more than one element in the queue, keep removing the elements
        while len(queue) > 1:
            # Since we're including the first element itself, we only need to shift k - 1 places
            toRemove = k - 1
            
            # While the elements to be removed are more than 0 then
            while (toRemove > 0):
                # Get the first element to shift to the back of the queue
                firstElem = queue.pop(0)
                # Append it to the back of the list
                queue.append(firstElem)
                # Decrement the counter
                toRemove -= 1
            # Pop the first element as it has been eliminated
            queue.pop(0)
            
        # Finally return the last element remaining
        return queue[0]
            
        
            