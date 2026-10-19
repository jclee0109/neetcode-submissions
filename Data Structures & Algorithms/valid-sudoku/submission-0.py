class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(board[0:3][0:3])
        return self.row_valid(board) and self.col_valid(board) and self.grid_valid(board)

    def row_valid(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = board[i]
            cnt = 0
            row_set = set()
            for elem in row:
                if elem in ["1", "2", "3", "4","5","6","7","8","9"]:
                    row_set.add(int(elem))
                    cnt += 1
            if len(row_set) != cnt: # dup exists!
                return False
        else: 
            return True
    
    def col_valid(self, board: List[List[str]]) -> bool:
        board_inv = []
        for i in range(len(board)):
            board_inv.append([board[j][i] for j in range(len(board))])
        return self.row_valid(board_inv)
    
    def grid_valid(self, board:List[List[str]]) -> bool:
        grid = []
        for i in range(len(board)//3):
            for j in range(len(board)//3):
                matrix = [row[3*i:3*(i+1)] for row in board[3*j:3*(j+1)]]
                result = [element for row in matrix for element in row]
                grid.append(result)
        return self.row_valid(grid)
        