# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1

        n1 = list1
        n2 = list2
        head = ListNode(val=-1)
        p = head
        while n1 and n2:
            if n1.val < n2.val:
                p.next = n1
                p = p.next
                n1 = n1.next
            else:
                p.next = n2
                p = p.next
                n2 = n2.next
        if n1:
            p.next = n1
        else:
            p.next = n2

        return head.next
