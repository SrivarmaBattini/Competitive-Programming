# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head

        if not current or not current.next:
            return head

        while current is not None and current.next is not None:

            if current.val == current.next.val:
                node = current.next

                while node is not None:
                    if node.val == current.val:
                        node = node.next
                    else:
                        current.next = node
                        break
                    
                    if node is None:
                        current.next = node
            
            current = current.next
        
        return head