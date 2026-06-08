class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lw = []
        up = []
        piv = []

        for i in nums:
            if i<pivot:
                lw.append(i)
            elif i>pivot:
                up.append(i)
            else:
                piv.append(i)
        
        return (lw+piv+up)