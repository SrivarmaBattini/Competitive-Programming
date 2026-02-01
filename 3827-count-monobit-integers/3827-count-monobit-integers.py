class Solution:
    def countMonobit(self, n: int) -> int:

        res = 2

        if n == 0:
            return 1
        elif n == 1:
            return 2
            
        for i in range(2, n+1):
            lt = []
            while i > 0:
                lt.append(i % 2)
                i = i // 2

            flag = True
            for j in range(1, len(lt)):
                if lt[j] != lt[j-1]:
                    flag = False
                    break

            if flag:
                res += 1
        return res