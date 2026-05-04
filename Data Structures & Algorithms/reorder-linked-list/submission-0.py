# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next

        i = 0
        n = len(nodes) - 1
        while i < n:
            nodes[i].next = nodes[n]
            i += 1
            if i >= n:
                break
            nodes[n].next = nodes[i]
            n -= 1
        nodes[i].next = None

            
        
