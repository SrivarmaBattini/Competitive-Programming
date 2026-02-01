class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        first = nums[0]
        arr = nums[1:]
        second = min(arr)
        arr.remove(second)
        third = min(arr)

        return first + second + third