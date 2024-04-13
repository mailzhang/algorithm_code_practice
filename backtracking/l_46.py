import copy


class Solution(object):

    def all_sort(self, unused, used):
        if len(unused) == 0:
            self.all_list.append(copy.deepcopy(used))
            return

        _used = copy.deepcopy(unused)

        for i in _used:
            used.append(i)
            unused.remove(i)
            self.all_sort(unused, used)
            used.remove(i)
            unused.append(i)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.all_list = []
        nums = nums

        self.all_sort(nums, [])
        return self.all_list


if __name__ == "__main__":
    nums = [1, 2, 3]
    r = Solution().permute(nums)
    print(r)
