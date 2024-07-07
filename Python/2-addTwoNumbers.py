# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create dummy node to handle edge cases of inserting to node
        dummy = ListNode()
        cur = dummy
        # Create variable to hold the carry forwards value
        carry = 0
        
        # Keep iterating until l1 or l2 is not null
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # New digit 
            val = v1 + v2 + carry
            # Handle the new carry
            carry = val // 10
            # Get the new digit to push to the list
            val = val % 10
            cur.next = ListNode(val)
            
            # Updated pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
            
            
            
            