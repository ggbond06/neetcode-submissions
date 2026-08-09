# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        output = ListNode()
        curr_output = output
        
        curr1 = list1
        curr2 = list2
        while curr1 is not None and curr2 is not None:

            if curr1.val < curr2.val:
                curr_output.next = curr1
                curr1 = curr1.next
            elif curr2.val < curr1.val:
                curr_output.next = curr2
                curr2 = curr2.next
            else:
                curr_output.next = curr1
                curr1 = curr1.next

            curr_output = curr_output.next

        if curr1 is not None:
            curr_output.next = curr1
        if curr2 is not None:
            curr_output.next = curr2

        return output.next