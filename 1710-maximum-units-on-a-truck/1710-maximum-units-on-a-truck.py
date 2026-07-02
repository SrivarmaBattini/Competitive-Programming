class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        res = 0
        
        for box in boxTypes:
            if truckSize <= 0:
                break
            
            n, u = box[0], box[1]
            if n <= truckSize:
                res += n*u
            else:
                res += truckSize * u
            truckSize -= n
        return res