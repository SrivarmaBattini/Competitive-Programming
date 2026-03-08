class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        
        n = len(nums)

        pre = [0] * n
        post = [0] * n

        pre[0] = 0
        post[n - 1] = 1

        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i - 1]

        ans = n

        if pre[n - 1] == 1:
            ans = n - 1

        for i in range(n - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]

            if post[i] == pre[i]:
                ans = i

            if post[i] > pre[i]:
                if ans != n:
                    return ans
                else:
                    return -1

        return -1


        # dp_sum = [0] * (len(nums) + 1)
        # for i in range(len(nums)):
        #     dp_sum[i+1] = dp_sum[i] + nums[i]
    
        # dp_prod = 1
        # for num in nums:
        #     dp_prod *= num

        # for k in range(len(nums)):
        #     dp_prod //= nums[k]
        #     if dp_sum[k] == dp_prod:
        #         return k

        # return -1

        # dp_prod = [1] * (len(nums) + 2)
        # for j in range(len(nums) - 1, -1, -1):
        #     dp_prod[j] = dp_prod[j+1] * nums[j]
        
        # for k in range(len(nums)):
        #     if dp_sum[k] == dp_prod[k+1]:
        #         return k
        # return -1