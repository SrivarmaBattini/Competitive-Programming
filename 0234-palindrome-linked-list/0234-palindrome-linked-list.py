# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return True

        def reverse(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev
        

        first_half = head
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second_half = reverse(slow)

        while second_half:
            if second_half.val != first_half.val:
                return False
            second_half = second_half.next
            first_half = first_half.next
        return True