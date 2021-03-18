class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0:
            return False

        row = len(matrix)
        col = len(matrix[0])

        l = 0
        r = row * col - 1

        while l <= r:
            m = l + (r - l) // 2
            element = matrix[m // col][m % col]
            if element == target:
                return True
            elif element > target:
                r = m - 1
            else:
                l = m + 1

        return False