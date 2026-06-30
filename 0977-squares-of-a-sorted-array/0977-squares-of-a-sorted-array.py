class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        pos = 0
        n = len(nums)

        for num in nums:
            if num <= 0:
                pos += 1
            else:
                break

        if pos == n:
            return [num * num for num in reversed(nums)]

        neg = pos - 1

        while neg >= 0 and nums[neg] == 0:
            neg -= 1

        if neg == -1:
            return [num * num for num in nums]

        diff = pos - neg - 1
        res = [0] * diff

        while pos < n or neg >= 0:
            if pos == n:
                res.append(nums[neg] * nums[neg])
                neg -= 1
            elif neg == -1:
                res.append(nums[pos] * nums[pos])
                pos += 1
            else:
                if nums[pos] < abs(nums[neg]):
                    res.append(nums[pos] * nums[pos])
                    pos += 1
                else:
                    res.append(nums[neg] * nums[neg])
                    neg -= 1

        return res