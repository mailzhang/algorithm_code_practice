class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        sum = 0
        for item in hours:
            if item >= target:
                sum += 1

        return sum


if __name__ == '__main__':
    hours = [0, 1, 2, 3, 4]
    target = 2
    r = Solution().numberOfEmployeesWhoMetTarget(hours, target)
    print(r)
