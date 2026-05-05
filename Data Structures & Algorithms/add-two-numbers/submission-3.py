# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_ = 0
        i = 1
        cur1 = l1
        cur2 = l2

        while cur1 or cur2:
            if cur1 and cur2:
                sum_ += cur1.val * i + cur2.val * i
                cur1 = cur1.next
                cur2 = cur2.next
            elif cur1:
                sum_ += cur1.val * i
                cur1 = cur1.next
            else:
                sum_ += cur2.val * i
                cur2 = cur2.next
            i *= 10
        
        nodes = []
        if sum_ == 0:
            return ListNode(0)
        while sum_ > 0:
            val = sum_ % 10
            nodes.append(ListNode(val))
            sum_ = sum_ // 10

        for i in range(1, len(nodes)):
            nodes[i - 1].next = nodes[i]
        
        return nodes[0]

        