# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        n = len(values)
        max_twin = 0

        for i in range(n//2):
            twin_sum = values[i] + values[n - i - 1]
            max_twin = max(max_twin, twin_sum)
        return max_twin
