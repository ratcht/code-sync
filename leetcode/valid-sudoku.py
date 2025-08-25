class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        quads = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".": continue
                # print(f"i: {i}. j: {j}. val: {board[i][j]}")

                # check row
                # rows[i] is current row
                if value in rows[i]:
                    return False
                rows[i].add(value)

                # check col
                if value in cols[j]:
                    return False
                cols[j].add(value)

                # check quadrant
                quad = floor(i / 3)*3 + floor(j / 3)
                if value in quads[quad]:
                    return False
                quads[quad].add(value)
                
        return True