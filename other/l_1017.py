class Solution(object):
    """
    TODO
    """
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 神仙解法
        # if n == 0:
        #     return '0'
        # res = []
        # while n:
        #     res.append(str(n & 1))
        #     n = -(n >> 1)
        # return ''.join(res[::-1])

        # 2   10   110
        # 3   11   111
        # 6   110
        res = []
        if n == 0:
            return '0'
        while n:
            remainder = n & 1
            res.append(str(remainder))
            n -= remainder
            n //= -2
        return ''.join(res[::-1])


if __name__ == '__main__':
    r = Solution().baseNeg2(2)
    print(r)
