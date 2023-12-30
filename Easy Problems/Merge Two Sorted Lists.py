# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, List1: Optional[ListNode], List2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #A dummy node is created. 
        tail = dummy #A tail node is initialized to point at the dummy node. This tail node will be used to build the merged list.

        while List1 and List2: #While not null (not empty)
            if List1.val < List2.val:
                tail.next = List1 #Adds List1's current node to the merged list
                List1 = List1.next #List1 is advanced to its next node
            else:
                tail.next = List2 #Adds List2's current node to the merged list
                List2 = List2.next #List2 is advanced to its next node
            tail = tail.next #This step is crucial to keep the tail at the end of the new merged list.
        
        if List1:
            tail.next = List1 #Still has nodes left, these nodes are appended to the merged list.
        elif List2:
            tail.next = List2 #Still has nodes left, these nodes are appended to the merged list.
        
        return dummy.next #The method returns the next node of the dummy node. This is the head of the new merged list.

'''
Example:

L1  = 1 2 4
L2  = 1 3 4

Output-->dummy-->1-->1-->2-->3-->4

'''
