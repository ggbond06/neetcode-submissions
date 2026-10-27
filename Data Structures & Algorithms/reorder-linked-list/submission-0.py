# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        temp = []

        curr = head

        while curr:
            temp.append(curr)
            curr = curr.next

        left = 0
        right = len(temp) - 1

        while left < right:
            temp[left].next = temp[right]
            left += 1
            
            if left == right:
                break
            
            temp[right].next = temp[left]
            right -= 1

        if temp:
            temp[left].next = None

        