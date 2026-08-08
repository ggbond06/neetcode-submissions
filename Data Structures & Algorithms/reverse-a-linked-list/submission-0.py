# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack_new = []
        
        if head is None: 
            return None

        current = head

        while current is not None:
            stack_new.append(current.val)
            current = current.next

        dummy = ListNode()
        current_new = dummy

        while stack_new:
            current_new.next = ListNode(stack_new.pop())
            current_new = current_new.next
        
        return dummy.next
            

        