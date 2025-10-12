# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # if not head or not head.next:
        #     return head
        
        # curr = head
        # output = ListNode(0)
        # dummy = output

        # while curr:
        #     if curr.next and curr.val == curr.next.val:
        #         while curr.next and curr.val == curr.next.val:
        #             curr = curr.next
        #     else:
        #         dummy.next = ListNode(curr.val)
        #         dummy = dummy.next
            
        #     curr = curr.next
        
        # return output.next


        dummy = ListNode(0, head)
        prev = dummy 
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                dup_val = curr.val
                while curr and curr.val == dup_val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return dummy.next