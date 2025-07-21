class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        def sumofdigits(number):
            res = 0
            while number > 0:
                res += number % 10
                number = number // 10
            return res

        for i in range(len(nums)):
            if sumofdigits(nums[i]) == i:
                return i
        else:
            return -1
            
        