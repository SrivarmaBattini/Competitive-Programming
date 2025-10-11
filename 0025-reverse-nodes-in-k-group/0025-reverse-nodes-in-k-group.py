# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # curr = head
        # nodes = 0
        # while curr:
        #     nodes += 1
        #     curr = curr.next
        
        # if nodes % k == 0:
        #     flag = True
        # else:
        #     flag = False
        # rep = nodes // k

        
        # current = head
        # iter = 0
        # for _ in range(rep):
            
        #     curr_head = current
        #     prev = None
        #     i = 1

        #     while i <= k and current is not None:
        #         next_node = current.next
        #         current.next = prev
        #         prev = current
        #         current = next_node
        #         i += 1
            
        #     if iter != 0:
        #         prev_head.next = prev
        #     iter += 1
        #     prev_head = curr_head

        #     if iter == rep and nodes % k != 0:
        #         prev_head.next = current
            
        # return head


        if not head or k == 0:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:

            kth = prev_group_end
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
                
            next_group_start = kth.next

            prev, curr = kth.next, prev_group_end.next
            while curr != next_group_start:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = prev_group_end.next
            prev_group_end.next = kth
            prev_group_end = temp
        
        return dummy.next