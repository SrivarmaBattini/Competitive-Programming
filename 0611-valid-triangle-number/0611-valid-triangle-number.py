class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        triangles = 0
        n = len(nums)
        nums.sort()
        
        for k in range(n-1,1,-1):

            i = 0
            j = k - 1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    triangles += (j - i)
                    j -= 1
                else:
                    i += 1
        
        return triangles