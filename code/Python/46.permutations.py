class Solution:
    # 递归
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        L = self.permute(nums[1:])
        res = []
        x = [nums[0]]
        for y in L:
            for i in range(len(y)+1):
                res.append(y[:i]+x+y[i:])
        res.sort()
        return res
