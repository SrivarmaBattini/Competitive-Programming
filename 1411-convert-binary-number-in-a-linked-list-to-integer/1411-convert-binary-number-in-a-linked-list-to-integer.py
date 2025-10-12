# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        decimal = 0
        nodes = 0
        
        current = head
        while current.next:
            nodes += 1
            current = current.next
        
        curr = head
        while curr:
            decimal += (curr.val * (2 ** nodes))
            nodes -= 1
            curr = curr.next
        
        return decimal