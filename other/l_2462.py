class Solution(object):

    def search_by_range(self, costs, start, end):
        _index = None
        _cost = float('inf')
        for _cost_i in range(start, end):
            if costs[_cost_i] < _cost:
                _cost = costs[_cost_i]
                _index = _cost_i
        return _cost, _index

    def _bfs(self, costs, k, candidates):
        if k == 0:
            return
        _index = None
        _cost = float('inf')
        if candidates < len(costs):
            _cost, _index = self.search_by_range(costs, 0, candidates)
            _cost1, _index1 = self.search_by_range(costs,  - candidates, 0)
            if _cost > _cost1:
                _cost = _cost1
                _index = _index1
        else:
            _cost, _index = self.search_by_range(costs, 0, len(costs))
        self.sum += _cost
        # print(_index, _cost)
        # print(costs)
        del costs[_index]
        self._bfs(costs, k - 1, candidates)

    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        self.sum = 0
        self._bfs(costs, k, candidates)

        return self.sum


if __name__ == '__main__':
    # leetcode 2462
    # costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
    # k = 3
    # candidates = 4
    # 11 TODO
    costs = [31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58]
    k = 11
    candidates = 2
    # 423
    r = Solution().totalCost(costs, k, candidates)
    print(r)
