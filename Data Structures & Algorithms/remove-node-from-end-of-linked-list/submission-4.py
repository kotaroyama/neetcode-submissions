# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        index = len(nodes) - n
        if index != 0:
            nodes[index - 1].next = nodes[index].next
        else:
            return head.next

        return nodes[0]