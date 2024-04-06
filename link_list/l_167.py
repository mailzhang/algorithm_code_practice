class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n1 = 0
        n2 = len(numbers) - 1
        while numbers[n1] + numbers[n2] != target:
            if n1 == n2:
                break
            if numbers[n1] + numbers[n2] < target:
                n1 = (n1 + n2) // 2
            else:
                n2 = (n1 + n2) // 2

        return [n1 + 1, n2 + 1]