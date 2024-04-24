class Solution(object):
    """
    滑动窗口
    """
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        # 因保持冷静导致满意的人 1
        _no_angry = 0

        i = 0
        j = 0
        _tmp = 0
        _start = 0
        n = len(customers)
        while j < n:
            if j < i + minutes:
                if grumpy[j] == 1:
                    _tmp += customers[j]
                j += 1
            if j == i + minutes:
                if _tmp > _no_angry:
                    _no_angry = _tmp
                    _start = i
                if grumpy[i] == 1:
                    _tmp -= customers[i]
                i += 1
        _res = 0
        for index, _cus in enumerate(customers):
            if grumpy[index] == 0 or (_start <= index < _start + minutes):
                _res += _cus
        print('_', _start)
        return _res


if __name__ == '__main__':
    customers = [1,0,1,2,1,1,7,5]
    grumpy = [0,1,0,1,0,1,0,1]
    minutes = 3
    r = Solution().maxSatisfied(customers, grumpy, minutes)
    print(r)
