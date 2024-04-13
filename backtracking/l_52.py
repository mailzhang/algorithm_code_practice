"""
https://leetcode.cn/problems/n-queens-ii/description/
"""


class Solution(object):

    def is_valid(self, tmp, row, col):
        # 上方同一列
        for i in range(row):
            if tmp[i][col] == 'Q':
                return False

        # 左上方
        r = row - 1
        l = col - 1
        while r >= 0 and l >= 0:
            if tmp[r][l] == 'Q':
                return False
            r -= 1
            l -= 1

        # 右上方
        r = row - 1
        l = col + 1
        n = len(tmp)
        while r >= 0 and l < n:
            if tmp[r][l] == 'Q':
                return False
            r -= 1
            l += 1

        return True

    def queen(self, tmp, row):
        n = len(tmp)
        if row == n:
            self.queen_count += 1
            return

        for i in range(n):
            if self.is_valid(tmp, row, i):
                tmp[row][i] = 'Q'
                self.queen(tmp, row+1)
                tmp[row][i] = '.'


    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.queen_count = 0
        tmp = [['.'] * n for _ in range(n)]
        self.queen(tmp, 0)
        return self.queen_count


if __name__ == '__main__':
    n = 4
    r = Solution().totalNQueens(n)
    print(r)
