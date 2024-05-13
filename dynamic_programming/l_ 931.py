class Solution(object):

    def dp(self, matrix, row, col):
        if row < 0 or col < 0 or col >= len(matrix):
            return 66666
        if self.mem[row][col] != 66666:
            return self.mem[row][col]
        if row == 0:
            self.mem[row][col] = matrix[row][col]
            return self.mem[row][col]
        # print(row, col)
        _m = min(
            self.dp(matrix, row - 1, col - 1),
            self.dp(matrix, row - 1, col),
            self.dp(matrix, row - 1, col + 1),
        )
        self.mem[row][col] = matrix[row][col] + _m
        return self.mem[row][col]

    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        _n = len(matrix)
        self.mem = [[66666 for _ in range(_n)] for _ in range(_n)]

        _min = 66666
        for i in range(_n):
            self.dp(matrix, _n - 1, i)
            if _min > self.mem[_n - 1][i]:
                _min = self.mem[_n - 1][i]
        return _min


if __name__ == '__main__':
    matrix = [[2, 1, 3],
              [6, 5, 4],
              [7, 8, 9]]
    r = Solution().minFallingPathSum(matrix)
    print(r)
