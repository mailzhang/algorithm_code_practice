import copy


class Solution(object):

    def is_repeat(self, tmp):
        for _arr in self.res:
            if sorted(_arr) == sorted(tmp):
                return True
        return False

    def backtracking(self, candidates, sum, tmp):
        if sum == 0 and not self.is_repeat(tmp):
            self.res.append(copy.deepcopy(tmp))
        elif sum < 0:
            return

        for i in candidates:
            tmp.append(i)
            self.backtracking(candidates, sum - i, tmp)
            tmp.remove(i)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        tmp = []
        self.res = []
        self.backtracking(candidates, target, tmp)

        return self.res


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    r = Solution().combinationSum(candidates, target)
    print(f"r {r}")
