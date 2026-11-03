class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        res = 0
        max_e = max(nums)

        for num in nums:
            res += (max_e - num)
        return res