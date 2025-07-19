class Solution:
    def splitArray(self, nums: List[int]) -> int:
        
        def is_prime(num):
            if num <= 1:
                return False
            for i in range(2, int(num ** 0.5)+1):
                if num % i == 0:
                    return False
            return True

            
        res = 0
        for i in range(len(nums)):
            if is_prime(i):
                res -= nums[i]
            else:
                res += nums[i]

        return abs(res)