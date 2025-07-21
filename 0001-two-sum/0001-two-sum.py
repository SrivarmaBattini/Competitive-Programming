class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        number_ind = {}

        for i, num in enumerate(nums):
            if target - num in number_ind:
                return [i, number_ind[target - num]]
            number_ind[num] = i
        