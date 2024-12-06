# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(0)
        tail = dummyhead
        while list1 or list2:
            n1 = list1.val if list1 else 1000
            n2 = list2.val if list2 else 1000
            if n1<n2:
                tail.next = ListNode(n1)
                list1 = list1.next
            else:
                tail.next = ListNode(n2)
                list2 = list2.next
            tail = tail.next
        return dummyhead.next
        