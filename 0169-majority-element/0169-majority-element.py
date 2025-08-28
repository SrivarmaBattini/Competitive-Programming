class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq = dict()

        for num in nums:
            freq[num] = freq.setdefault(num, 0) + 1
        

        for u, v in freq.items():
            if v > len(nums) // 2:
                return u
        
        return -1