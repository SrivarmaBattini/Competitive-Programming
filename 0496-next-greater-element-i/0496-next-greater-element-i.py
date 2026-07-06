class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        next_greater_elm = {}

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater_elm[smaller] = num
            
            stack.append(num)
        
        while stack:
            next_greater_elm[stack.pop()] = -1

        return [next_greater_elm[num] for num in nums1]