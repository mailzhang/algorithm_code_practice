class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp_arr = [-99] * (n + 1)
        return self.dp(n, dp_arr)

    def dp(self, n, dp_arr):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if dp_arr[n] != -99:
            return dp_arr[n]

        dp_arr[n] = self.dp(n - 1, dp_arr) + self.dp(n - 2, dp_arr)

        return dp_arr[n]


if __name__ == '__main__':

    r = Solution().fib(4)
    print(r)