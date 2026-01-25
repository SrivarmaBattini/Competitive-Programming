class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        nni = []
        nni_Val = []

        for i in range(n):
            if nums[i] >= 0:
                nni.append(i)
                nni_Val.append(nums[i])

        if not nni:
            return nums
            
        rotate = k % len(nni)
        rnni = nni_Val[rotate:] + nni_Val[:rotate]

        for idx, val in zip(nni, rnni):
            nums[idx] = val

        return nums