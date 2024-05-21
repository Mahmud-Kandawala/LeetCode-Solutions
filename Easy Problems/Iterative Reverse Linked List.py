# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # T O(n)  M O(1)
        prev, curr = None, head #Will eventually point to the previous node, Set to head. This will point to the current node being processed (starting with the head of the list).
        
        while curr: #Loop is used to iterate through the list as long as curr is not None
            nxt = curr.next #Stores the next node in the list. This step is crucial because the link between nodes will be reversed, and we need to keep track of the next node to continue the iteration.
            curr.next = prev #This reverses the link of the current node, making it point to the previous node.
            prev = curr #prev is updated to curr. This moves the prev pointer one step forward to the current node, which will become the previous node in the next iteration.
            curr = nxt #curr is updated to nxt. This moves the curr pointer one step forward to the next node, allowing the loop to continue with the next node in the original list.
        return prev #After the loop completes, prev will be pointing to the new head of the reversed list. The method returns prev.

'''
Pure Code:

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 
        return prev 
'''
