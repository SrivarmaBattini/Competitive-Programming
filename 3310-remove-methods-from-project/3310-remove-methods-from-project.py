class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
        tree = {}
        for inv in invocations:
            a = inv[0]
            b = inv[1]
            if a not in tree:
                tree[a] = [b]
            else:
                tree[a].append(b)


        sus = set()
        stack = [k]
        while stack:
            node = stack.pop()
            if node in sus:
                continue
            
            sus.add(node)

            if node in tree:
                for nei in tree[node]:
                    if nei not in sus:
                        stack.append(nei)
        
        res = []
        for c in tree.keys():
            if c in sus:
                continue
            
            for nc in tree[c]:
                if nc in sus:
                    return [i for i in range(n)]
        
        for i in range(n):
            if i not in sus:
                res.append(i)
        return res