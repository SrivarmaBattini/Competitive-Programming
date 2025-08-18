class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        
        res = 0

        for i in range(32):
            count_ones = 0
            for num in nums:
                if (num >> i) & 1 :
                    count_ones += 1
            count_zeros = len(nums) - count_ones
            res += count_ones * count_zeros
        return res