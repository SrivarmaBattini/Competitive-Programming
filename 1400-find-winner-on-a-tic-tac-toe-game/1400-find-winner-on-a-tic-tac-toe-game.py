class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        board = [[""] * 3 for _ in range(3)]

        for i, (r, c) in enumerate(moves):
            if i % 2 == 0:
                board[r][c] = 'A'
            else:
                board[r][c] = 'B'
        
        def winner(player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2 - i] == player for i in range(3)):
                return True
            return False
        
        n = len(moves)
        if n < 5:
            return "Pending"
        
        if winner("A"):
            return "A"
        elif winner("B"):
            return "B"
        elif n == 9:
            return "Draw"
        else:
            return "Pending"