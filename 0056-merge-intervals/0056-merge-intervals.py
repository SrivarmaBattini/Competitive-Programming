class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals.sort()

        for inter in intervals:
            if len(res) == 0:
                res.append(inter)
            else:
                if inter[0] <= res[-1][1]:
                    if inter[1] >= res[-1][1]:
                        res[-1][1] = inter[1]
                    else:
                        continue
                else:
                    res.append(inter)

        return res