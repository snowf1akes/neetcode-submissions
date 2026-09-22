# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #fast and slow tech
        slow, fast = head, head
        while fast and fast.next: #if they aren't null, so its a cycle
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True
        return False



