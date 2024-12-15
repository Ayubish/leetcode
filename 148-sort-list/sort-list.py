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
        dummy = ListNode(0)
        tail = dummy
        for i in range(len(a)):
            tail.next = ListNode(a[i])
            tail = tail.next
        return dummy.next