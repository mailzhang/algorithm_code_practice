import copy


class Solution(object):

    def is_valid(self, tmp, row, col):
        for i in range(row):
            if tmp[i][col] == 'Q':
                return False
        # 左上方
        r = row - 1
        c = col - 1
        while r >= 0 and c >= 0:
            if tmp[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # 右上方
        r = row - 1
        c = col + 1
        while r >= 0 and c < len(tmp):
            if tmp[r][c] == 'Q':
                return False
            r -= 1
            c += 1

        return True

    def backtracking(self, tmp, row):
        for i in range(len(tmp)):
            if self.is_valid(tmp, row, i):
                tmp[row][i] = 'Q'
                if row == len(tmp) - 1:
                    self.q_list.append(["".join(_row) for _row in tmp])
                else:
                    self.backtracking(tmp, row + 1)

                tmp[row][i] = '.'

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.q_list = []
        tmp = [ ['.'] * n for _ in range(n)]
        self.backtracking(tmp, 0)

        return self.q_list


if __name__ == '__main__':
    # _s = [['.'] * 2] * 2  # 用这个报错 err
    # print(_s)
    # _s = [["."] * 2 for _ in range(2)] # 对的
    # print(_s)
    # _s[0][0] = 'Q'
    # print(_s)

    r = Solution().solveNQueens(4)
    print(r)
