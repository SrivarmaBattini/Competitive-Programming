class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        
        res = 0
        for i in range(len(arr1)):
            flag = False
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    flag = True
                    break
            
            if not flag and len(arr2) > 1:
                res += 1
        
        return res