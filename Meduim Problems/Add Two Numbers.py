# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: #In Python, a class is a blueprint for creating objects. Here, we define a class named Solution, which will contain methods (functions) to solve problems. It allows us to organize related code and logic together.
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode() # Acts as a placeholder at the beginning of the resulting linked list. 
        cur = dummy # Pointer to the dummy node.

        carry = 0 # Keeps track of the carry-over value when adding digits
        while l1 or l2 or carry: # The loop continues until l1, l2, and carry are all False or None
            v1 = l1.val if l1 else 0 #  Retrieve the values of the current nodes
            v2 = l2.val if l2 else 0 #  Retrieve the values of the current nodes
        
            val = v1 + v2 + carry #  Calculate the sum of the current digits

            carry = val // 10 # Update the carry variable with the value needed to carry over to the next addition 
            val = val % 10 #  Calculate the value that should be stored in the current node of the resulting linked list by taking the modulo 10 of the sum

            cur.next = ListNode(val) # Create a new node with the calculated value and attach it to the cur.next pointer

            cur = cur.next # Update the cur pointer to move it to the newly created node, as we are building the resulting linked list
            l1 = l1.next if l1 else None # Move the l1 and l2 pointers to their next nodes (if available) to progress through the input linked lists
            l2 = l2.next if l2 else None # Move the l1 and l2 pointers to their next nodes (if available) to progress through the input linked lists
        
        return dummy.next # Return the dummy.next pointer, which is the head of the resulting linked list containing the sum of the two input linked lists








        




    
 
