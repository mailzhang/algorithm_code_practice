class Solution(object):
    """
    明确 base case -> 明确「状态」-> 明确「选择」 -> 定义 dp 数组/函数的含义
    """

    def dp(self, index, nums):
        if index == 0:
            self.dp_arr[index] = 1
        if index == len(nums):
            return
        i = index - 1
        tmp = 1
        while i >= 0:
            if nums[i] < nums[index] and self.dp_arr[i] + 1 > tmp:
                tmp = self.dp_arr[i] + 1
            i -= 1
        self.dp_arr[index] = tmp
        self.dp(index + 1, nums)

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.dp_arr = [0 for _ in range(len(nums))]
        self.dp(0, nums)
        print(self.dp_arr)
        tmp = 1
        for i in self.dp_arr:
            if tmp < i:
                tmp = i
        return tmp


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    r = Solution().lengthOfLIS(nums)
    print(r)
