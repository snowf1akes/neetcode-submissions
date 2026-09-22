# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #edge cases, if list lenght is 0, or is null
        if not lists or len(lists) == 0: 
            return None #empty linked list
        while len(lists) > 1: #until theres only 1 list left
            mergedList = [] 

            for i in range(0, len(lists), 2): #start, end, incrementor 2 for pairs
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                mergedList.append(self.mergeList(l1, l2))
            lists = mergedList
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

            
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next