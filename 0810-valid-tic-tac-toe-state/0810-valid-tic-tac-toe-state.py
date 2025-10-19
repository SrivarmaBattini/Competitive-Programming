class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)

        if not (x_count == o_count or o_count + 1 == x_count):
            return False
        
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
        
        player_o = winner('O')
        player_x = winner('X')

        if player_o and player_x:
            return False
        if player_x and x_count != o_count + 1:
            return False
        if player_o and x_count != o_count:
            return False
        return True