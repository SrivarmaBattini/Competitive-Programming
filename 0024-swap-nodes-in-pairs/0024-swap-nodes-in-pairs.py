# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_end = dummy

        while True:
            second = prev_end
            for _ in range(2):
                second = second.next
                if not second:
                    return dummy.next
            
            next_start = second.next

            prev = second.next
            curr = prev_end.next

            while curr != next_start:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prev_end.next
            prev_end.next = second
            prev_end = temp
        
        return dummy.next
