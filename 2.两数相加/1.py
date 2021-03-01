# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 迭代法
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        total = 0
        next1 = 0
        result = ListNode()
        cur = result
        while l1 != None and l2 != None:
            total = l1.val + l2.val + next1
            cur.next = ListNode(val=total % 10)
            next1 = total // 10
            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        while l1 != None:
            total = l1.val + next1
            cur.next = ListNode(val=total % 10)
            next1 = total // 10
            l1 = l1.next
            cur = cur.next

        while l2 != None:
            total = l2.val + next1
            cur.next = ListNode(val=total % 10)
            next1 = total // 10
            l2 = l2.next
            cur = cur.next

        if next1 != 0:
            cur.next = ListNode(val=next1)

        return result.next
