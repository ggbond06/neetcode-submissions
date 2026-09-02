# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy

        curr1 = l1
        curr2 = l2
        carry = 0

        while curr1 and curr2:
            sum = curr1.val + curr2.val + carry
            carry = sum // 10
            digit = sum % 10
            
            tail.next = ListNode(digit)

            tail = tail.next

            curr1 = curr1.next
            curr2 = curr2.next

        if tail.next is None and carry == 1:
            tail.next = ListNode(1)

        while curr1 or curr2 or carry == 1:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            sum = val1 + val2 + carry
            carry = sum // 10
            digit = sum % 10

            tail.next = ListNode(digit)
            tail = tail.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        
        return dummy.next

