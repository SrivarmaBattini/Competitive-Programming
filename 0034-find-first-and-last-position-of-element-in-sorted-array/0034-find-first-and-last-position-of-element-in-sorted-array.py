class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        first = -1
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        

        last = -1
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        

        return [first, last]