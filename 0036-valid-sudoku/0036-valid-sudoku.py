class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkrow(board):
            for i in range(len(board)):
                freq = dict()
                for j in range(len(board)):
                    if board[i][j] == ".":
                        continue
                    freq[board[i][j]] = freq.setdefault(board[i][j], 0) + 1
                    if freq[board[i][j]] > 1:
                        return False
            return True
        
        def checkcol(board):
            for j in range(len(board)):
                freq = dict()
                for i in range(len(board)):
                    if board[i][j] == ".":
                        continue
                    freq[board[i][j]] = freq.setdefault(board[i][j], 0) + 1
                    if freq[board[i][j]] > 1:
                        return False
            return True

        def checkboxes(board):
            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    freq = dict()
                    for i in range(3):
                        for j in range(3):
                            val = board[box_row + i][box_col + j]
                            if val == ".":
                                continue
                            freq[val] = freq.setdefault(val, 0) + 1
                            if freq[val] > 1:
                                return False
            return True

        return checkrow(board) and checkcol(board) and checkboxes(board)
