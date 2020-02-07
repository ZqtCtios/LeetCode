class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        indexSum = len(nums)/2
        res = []
        for i in range(indexSum):
            a = nums[2*i]
            b = nums[2*i+1]
            for i in range(a):
                res.append(b)
        return res
