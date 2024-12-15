# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        tail = head
        while tail:
            a.append(tail.val)
            tail = tail.next
        a.sort()
        tail = head
        for i in a:
            tail.val = i
            tail = tail.next
        return head