# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        temp = head
        count = 0
        if length == n:
            return head.next
        while temp.next:
            
            if count == length-n-1:
                print(temp.val)
                temp.next = temp.next.next
                return head
            temp = temp.next
            count += 1
        