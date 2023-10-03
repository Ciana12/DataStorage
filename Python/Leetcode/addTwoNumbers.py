#zukarin is here
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)  # Dummy node to simplify the implementation
        current = dummy  # Pointer to the current node
        carry = 0  # Variable to store the carry value
        
        while l1 or l2:
            # Get the values of the current nodes (or 0 if the list has ended)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create a new node with the sum digit and update the current node
            current.next = ListNode(digit)
            current = current.next
            
            # Move to the next nodes in the input lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # If there is a remaining carry, create a new node with its value
        if carry != 0:
            current.next = ListNode(carry)
        
        return dummy.next
