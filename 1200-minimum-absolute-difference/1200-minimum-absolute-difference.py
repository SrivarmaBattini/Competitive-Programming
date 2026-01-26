class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        mini = float('inf')
        res = []

        for i in range(1, len(arr)):
            if mini > (arr[i] - arr[i - 1]):
                mini = arr[i] - arr[i - 1]
                res = []
                res.append([arr[i - 1], arr[i]])
            elif mini == (arr[i] - arr[i - 1]):
                res.append([arr[i - 1], arr[i]])
        return res     