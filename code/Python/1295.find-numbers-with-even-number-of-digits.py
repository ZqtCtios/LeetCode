class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                sum += 1
        return sum
