# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head

        nodes = 0
        curr = head
        while curr:
            nodes += 1
            curr = curr.next
        
        dummy = ListNode(0)
        dummy.next = head

        if nodes == k or k % nodes == 0:
            return head
        
        prev = None
        curr = head
        
        k = k % nodes
        for _ in range(nodes - k):
            prev = curr
            curr = curr.next
        
        prev.next = None

        temp = curr
        while curr.next:
            curr = curr.next
        
        curr.next = dummy.next
        dummy.next = temp

        return dummy.next
    