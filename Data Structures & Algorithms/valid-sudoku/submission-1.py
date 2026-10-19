class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(len(board))]
        col = [set() for _ in range(len(board))]
        box = [set() for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                box_idx = 3*(i//3) + j//3 #3n + m (box flatten)

                if board[i][j] in row[i]:
                    print("row", row)
                    return False # already exist in row
                if board[i][j] in col[j]:
                    print("col", col)
                    return False # exist in col
                if board[i][j] in box[box_idx]:
                    print("box", box)
                    return False # exist in box

                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[box_idx].add(board[i][j])

        
        return True