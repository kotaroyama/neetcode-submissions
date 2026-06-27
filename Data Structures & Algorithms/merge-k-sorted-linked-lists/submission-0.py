# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tmp_list = []
        
        for l in lists:
            while l:
                tmp_list.append(l.val)
                l = l.next
        tmp_list.sort()

        result = ListNode(0)
        current = result
        for item in tmp_list:
            current.next = ListNode(item)
            current = current.next
        
        return result.next
        

        