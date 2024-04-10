class Solution(object):

    def dp(self, coins, amount, dp_arr):

        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if dp_arr[amount] != -99:
            return dp_arr[amount]

        tmp_min = float('inf')
        for coin in coins:
            res = self.dp(coins, amount - coin, dp_arr)

            if res == -1:
                continue

            tmp_min = min(tmp_min, res + 1)

        dp_arr[amount] = tmp_min if tmp_min != float('inf') else -1
        return dp_arr[amount]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp_arr = [-99] * (amount + 10)
        min_amount = self.dp(coins, amount, dp_arr)

        return min_amount


if __name__ == '__main__':
    coins = [5, 1, 2, ]
    amount = 30
    r = Solution().coinChange(coins, amount)
    print(r)
