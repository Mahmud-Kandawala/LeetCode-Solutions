# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive T O(n),  M O(n)

        if not head: #This checks if head is None (i.e., the linked list is empty). If it is, the method returns None, as there's nothing to reverse.
            return None

        newHead = head #This initializes newHead to be the same as head. This is a temporary assignment and will be updated if the list has more nodes.
        
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head 
            
            '''
            This checks if the current node (head) has a next node.
            If it does, the method recursively calls itself with head.next 
            (i.e., the next node in the list). The result of this 
            recursive call (which will eventually be the new head of 
            the reversed list) is assigned to newHead.

           After the recursive call returns, head.next.next = head sets the 
           next node's next reference to point back to the current node 
           (head). This effectively reverses the link between the current 
           node  and the next node.
            '''
        
        head.next = None #This line sets the next reference of the current node to None. This is necessary to avoid forming a cycle in the list. When the recursion reaches the original tail of the list, this ensures the new tail's next pointer is None.
       
        return newHead #The method returns newHead, which is the new head of the reversed linked list.


'''
Pure Code:

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head 
        head.next = None

        return newHead 
        
'''
