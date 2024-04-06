# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        _i = 0
        pre = ListNode(-1, head)
        fast = pre
        slow = pre
        while fast.next:
            fast = fast.next
            _i += 1

            if _i > n:
                slow = slow.next
        _t = slow.next
        slow.next = slow.next.next
        _t.next = None

        return pre.next

