# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        # head removal
        if length == n:
            return head.next
        # traverse
        current = head
        for _ in range(length - n - 1):
            current = current.next

        current.next = current.next.next
        return head
