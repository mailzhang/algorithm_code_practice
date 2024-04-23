class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        _no_angry = 0
        for i in range(len(customers)):
            _tmp_no = 0
            for j in range(len(customers)):
                if i <= j < i + minutes:
                    _tmp_no += customers[j]
                elif grumpy[j] == 0:
                    _tmp_no += customers[j]
            if _no_angry < _tmp_no:
                _no_angry = _tmp_no

        return _no_angry


if __name__ == '__main__':
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    minutes = 1
    r = Solution().maxSatisfied(customers, grumpy, minutes)
    print(r)
