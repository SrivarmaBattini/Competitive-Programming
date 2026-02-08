class Solution:
    def check(self, nums: List[int]) -> bool:
        
        # m = min(nums)
        # mi = nums.index(m)
        
        # for i in range(1, len)

        # for i in range(mi, mi + len(nums) - 1):
        #     if nums[i % len(nums)] > nums[(i + 1) % len(nums)]:
        #         return False
        # return True

        arr = nums + nums
        n = 0
        for i in range(len(arr) - 1):
            if n == len(nums) - 1:
                return True
            
            if arr[i] <= arr[i + 1]:
                n += 1
            else:
                n = 0
        return False
