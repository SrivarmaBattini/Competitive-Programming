class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        cost_matrix = [[float('inf') for _ in range(26)] for _ in range(26)]

        for i in range(26):
            cost_matrix[i][i] = 0
        
        for i in range(len(original)):
            x = ord(original[i]) - 97
            y = ord(changed[i]) - 97
            z = cost[i]
            cost_matrix[x][y] = min(cost_matrix[x][y], z)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][k] + cost_matrix[k][j])
        

        min_cost = 0
        for i in range(len(source)):
            
            x = ord(source[i]) - 97
            y = ord(target[i]) - 97

            if cost_matrix[x][y] == float('inf'):
                return -1
            
            min_cost += cost_matrix[x][y]
        
        return min_cost