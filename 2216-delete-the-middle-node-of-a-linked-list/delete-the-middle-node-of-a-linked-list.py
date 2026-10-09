# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return
        count = 0
        copy = head
        while copy:
            count += 1
            copy = copy.next

        middle = (count // 2) - 1
        copy = head
        for _ in range(middle):
            copy = copy.next
        copy.next = copy.next.next
        return head