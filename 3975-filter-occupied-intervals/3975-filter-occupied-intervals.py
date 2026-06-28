class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:

        n = len(occupiedIntervals)
        if not occupiedIntervals: return []
        occupiedIntervals.sort()
        merged = [occupiedIntervals[0]]
        
        for i in range(1, n):
            interval = occupiedIntervals[i]
            if merged[-1][1] <= interval[1] and merged[-1][1] >= (interval[0]-1):
                merged[-1][1] = interval[1]
            elif merged[-1][-1] >= interval[1] and merged[-1][1] >= interval[0]:
                continue
            else:
                merged.append(interval)

        ans = []
        for start, end in merged:

            if end < freeStart or start > freeEnd:
                ans.append([start, end])
            elif start >= freeStart and end <= freeEnd:
                continue
            elif start < freeStart <= end <= freeEnd:
                ans.append([start, freeStart - 1])
            elif freeStart <= start <= freeEnd < end:
                ans.append([freeEnd + 1, end])
            else:
                ans.append([start, freeStart - 1])
                ans.append([freeEnd + 1, end])

        return ans