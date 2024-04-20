class Solution(object):
    """
    数组排序；相邻相等的跳过
    """

    def is_repeat(self, tmp):
        for _arr in self.res:
            if len(tmp) == len(_arr) and sorted(_arr) == sorted(tmp):
                return True
        return False

    def backtracking(self, candidates, target, tmp, index):

        if target == 0 and not self.is_repeat(tmp):
            self.res.append(tmp[:])
        elif target < 0:
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            tmp.append(candidates[i])
            self.backtracking(candidates, target - candidates[i], tmp, i + 1)
            tmp.remove(candidates[i])

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        tmp = []
        self.res = []
        candidates.sort()
        self.backtracking(candidates, target, tmp, 0)
        return self.res


if __name__ == '__main__':
    # candidates = [10, 1, 2, 7, 6, 1, 5]
    # target = 8
    candidates = [1, 2]
    target = 2
    r_ = Solution().combinationSum2(candidates, target)
    print(r_)
