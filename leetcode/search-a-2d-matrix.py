class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search the columns. binary search the rows

        while len(matrix) > 1:
            row_i = len(matrix) // 2
            row = matrix[row_i]
            last = row[-1]
            first = row[0]
            # hit target
            if last == target or first == target:
                return True
            
            # greater than target -> target in lower half of rows
            if target < last and target > first:
                matrix = [matrix[row_i]]
            elif target < last:
                matrix = matrix[:row_i]
            elif target > last:
                matrix = matrix[row_i+1:]
        
        # now, just binary search the row

        print(f"matrix: {matrix}")
        if not matrix:
            return False
        row = matrix[0]

        while len(row) >= 1:
            i = len(row) // 2

            if row[i] == target:
                return True
            elif row[i] > target:
                row = row[:i]
            else:
                row = row[i+1:]

        print(row)
        if row:
            return row[0] == target
        return False