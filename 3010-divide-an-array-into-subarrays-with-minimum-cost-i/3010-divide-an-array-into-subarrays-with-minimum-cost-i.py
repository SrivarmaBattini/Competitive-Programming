class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        first = nums[0]
        # arr = nums[1:]
        # second = min(arr)
        # arr.remove(second)
        # third = min(arr)
        
        second = float('inf')
        third = float('inf')

        for num in nums[1:]:
            if num < second:
                third = second
                second = num
            elif num >= second and num < third:
                third = num

        return first + second + third