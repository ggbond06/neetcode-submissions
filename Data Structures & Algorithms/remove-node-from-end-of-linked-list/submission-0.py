# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        total = 0

        while curr:
            total += 1
            curr = curr.next;
        curr = head
        delete_position = total - n
        temp = 0
        while curr:
            if delete_position == 0:
                head = curr.next
                break
            if temp == delete_position - 1:
                curr.next = curr.next.next
                break
            temp += 1
            curr = curr.next

        return head
                



