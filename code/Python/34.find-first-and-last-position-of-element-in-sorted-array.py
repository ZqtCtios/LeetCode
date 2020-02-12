class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        bottom, top = 0, len(nums)-1
        while bottom <= top:
            mid = (bottom+top)//2
            if nums[mid] == target:
                i, j = mid, mid
                while i <= len(nums)-1 and nums[i] == target:
                    i += 1
                while j >= 0 and nums[j] == target:
                    j -= 1
                return [j+1, i-1]
            elif nums[mid] > target:
                top = mid-1
            elif nums[mid] < target:
                bottom = mid+1
        return [-1, -1]
