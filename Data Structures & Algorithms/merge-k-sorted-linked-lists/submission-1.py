# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            head = ListNode(0)
            cur = head

            while list1 or list2:
                if list1 and list2:
                    if list1.val <= list2.val:
                        cur.next = ListNode(list1.val)
                        cur = cur.next
                        list1 = list1.next
                    else:
                        cur.next = ListNode(list2.val)
                        cur = cur.next
                        list2 = list2.next
                else:
                    if list1:
                        cur.next = ListNode(list1.val)
                        cur = cur.next
                        list1 = list1.next
                    if list2:
                        cur.next = ListNode(list2.val)
                        cur = cur.next
                        list2 = list2.next
            
            return head.next
        
        if not lists: return None

        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i - 1], lists[i])
        
        return lists[-1]