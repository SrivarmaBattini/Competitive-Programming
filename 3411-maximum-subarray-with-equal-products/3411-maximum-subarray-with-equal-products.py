class Solution:
    def maxLength(self, nums: List[int]) -> int:

        def lcm(a, b):
            return (a * b) // gcd(a, b)
        
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        
        n = len(nums)
        res = 0

        for i in range(n):
            prod = 1
            gc = 0
            lc = 1

            for j in range(i, n):
                ele = nums[j]

                prod *= ele
                gc = gcd(gc, ele)
                lc = lcm(lc, ele)

                if prod == gc * lc:
                    res = max(res, j - i + 1)

        return res