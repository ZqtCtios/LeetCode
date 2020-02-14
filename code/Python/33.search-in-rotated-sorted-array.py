class Solution:
    def search(self, nums, target: int) -> int:
        l = 0
        n = len(nums)
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[l]:
                # 左边乱序
                if nums[mid] < target and nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                # 右边乱序
                if nums[mid] > target and nums[l] <= target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
