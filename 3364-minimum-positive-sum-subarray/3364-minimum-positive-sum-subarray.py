class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        res = float('inf')
        for i in range(l, r + 1):
            for j in range(i, len(nums)+1):
                curr = sum(nums[j-i: j])
                if curr > 0:
                    res = min(res, curr)
        return -1 if res == float("inf") else res