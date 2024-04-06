# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        a1 = headA
        b1 = headB
        a1_f = False
        b1_f = False
        while a1 and b1:
            if a1 == b1:
                return a1

            a1 = a1.next
            b1 = b1.next
            if not a1 and not a1_f:
                a1_f = True
                a1 = headB
            if not b1 and not b1_f:
                b1_f = True
                b1 = headA

        return None


