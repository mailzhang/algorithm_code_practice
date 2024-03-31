class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1

        # 左侧边界
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if left < 0 or left >= len(nums):
            _left =  -1
        else:
            _left = left if nums[left] == target else -1


        # 右侧边界
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                 left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if right < 0 or right >= len(nums):
            _right = -1
        else:
            _right = right if nums[right] == target else -1

        return [_left, _right]



if __name__ == '__main__':
    nums = [5,7,7,8,8,8,8,10]
    target = 8
    res_ = Solution().searchRange(nums,target)
    print(res_)
