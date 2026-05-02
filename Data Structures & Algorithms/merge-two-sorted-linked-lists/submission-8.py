# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        cur1 = list1
        cur2 = list2
        while cur1 or cur2:
            if cur1 is None:
                result.append(cur2)
                cur2 = cur2.next
                continue
            if cur2 is None:
                result.append(cur1)
                cur1 = cur1.next
                continue
            if cur1.val == cur2.val:
                result.append(cur1)
                result.append(cur2)
                cur1 = cur1.next
                cur2 = cur2.next
            elif cur1.val < cur2.val:
                result.append(cur1)
                cur1 = cur1.next
            else:
                result.append(cur2)
                cur2 = cur2.next
        for i in range(len(result) - 1):
            result[i].next = result[i+1]
        if not result:
            return list1
        return result[0]
        
            


            
        
