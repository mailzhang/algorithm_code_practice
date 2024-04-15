import copy


class Solution(object):

    def is_exist(self, tmp):
        for item in self.valid_list:
            if tmp[0] in item and tmp[1] in item and tmp[2] in item:
                return True

        return False

    def backtracking(self, k, n, start, tmp, unuse):
        # if k == 0 and n == 0 and not self.is_exist(tmp):
        if k == 0 and n == 0:
            self.valid_list.append(copy.copy(tmp))
        elif k <= 0 or n < 0:
            return

        for i in range(start, len(unuse)):
            tmp.append(unuse[i])
            self.backtracking(k - 1, n - unuse[i], i + 1, tmp, unuse)
            tmp.remove(unuse[i])

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.valid_list = []
        self.total = k
        tmp = []
        unuse = [i for i in range(1, 10)]
        self.backtracking(k, n, 0, tmp, unuse)

        return self.valid_list


if __name__ == '__main__':
    k = 4
    n = 54
    r = Solution().combinationSum3(k, n)
    print(f"r {r}")
