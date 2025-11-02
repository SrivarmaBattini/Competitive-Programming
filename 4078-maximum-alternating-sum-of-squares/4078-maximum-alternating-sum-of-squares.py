class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        arr = [abs(num) for num in nums]
        arr.sort()

        i = 0
        j = len(arr) - 1
        res = 0
        while i < j:

            res += ((arr[j] ** 2) - (arr[i] ** 2))
            i += 1
            j -= 1

        if i == j:
            res += (arr[j] ** 2)
    
        return res