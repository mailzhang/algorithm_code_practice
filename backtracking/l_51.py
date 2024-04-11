import copy


class Solution(object):

    def is_valid(self, tmp, row, col):
        for i in range(row):
            if tmp[i][col] == 'Q':
                return False
        # 左上方
        r = row
        c = col
        while r >= 0 and c >= 0:
            if tmp[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # 右上方
        r = row
        c = col
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
                    self.q_list.append(copy.deepcopy(tmp))
                else:
                    self.backtracking(tmp, row + 1)

                tmp[row][i] = '.'

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.q_list = []
        tmp = [['*'] * n] * n
        self.backtracking(tmp, 0)

        return self.q_list


if __name__ == '__main__':
    # print([['*'] * 2] * 2)
    r = Solution().solveNQueens(4)
    print(r)
