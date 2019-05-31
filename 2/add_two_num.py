# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    @staticmethod
    def checkLength(l: ListNode) -> int:
        cnt = 0
        while l.next is not None:
            cnt += 1
            l = l.next
        return cnt

    @staticmethod
    def finalCheck(l: ListNode) -> ListNode:
        start_node = l
        while True:
            if l.val < 10:
                if l.next is None:
                    break
                l = l.next
                continue
            l.val -= 10
            if l.next is None:
                l.next = ListNode(1)
                break
            else:
                l.next.val += 1
            l = l.next
        return start_node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_len = self.checkLength(l1)
        l2_len = self.checkLength(l2)
        if l2_len > l1_len:
            tmp = l2
            l2 = l1
            l1 = tmp
        start_node = l1
        cur_node = l1
        while True:
            cur_node.val += l2.val
            if l2.next is None:
                break
            l1 = cur_node
            l1 = l1.next
            l2 = l2.next
            cur_node = cur_node.next

        return self.finalCheck(start_node)
