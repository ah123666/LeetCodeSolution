# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        while head is not None and head.next is not None:
            dnext = dummy.next
            hnext = head.next
            dummy.next = hnext
            head.next = hnext.next
            hnext.next = dnext

        return dummy.next
    def reverseList_digui(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        p = self.reverseList_digui(head.next)
        head.next.next = head
        head.next = None
        return p