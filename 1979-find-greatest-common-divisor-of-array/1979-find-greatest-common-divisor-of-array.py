class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxi,mini=min(nums),max(nums)
        def gcd(a,b):
            if b==0:
                return a
            else:
                return gcd(b,a%b)
        return gcd(mini,maxi)