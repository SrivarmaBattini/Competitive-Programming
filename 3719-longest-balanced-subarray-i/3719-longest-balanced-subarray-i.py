class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0

        for l in range(n):
            even = set()
            odd = set()

            for r in range(l, n):
                if nums[r] % 2 == 0:
                    even.add(nums[r])
                else:
                    odd.add(nums[r])
                
                if len(even) == len(odd):
                    res = max(res, r - l + 1)
        
        return res