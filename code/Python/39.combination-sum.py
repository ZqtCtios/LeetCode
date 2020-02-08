class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.L = []
        self.candidates = candidates
        self.search(target)
        return self.L

    def search(self, target, a=[]):
        for x in self.candidates:
            if len(a) == 0 or x >= a[-1]:
                if x == target:
                    a.append(x)
                    self.L.append(a)
                    break
                elif x < target:
                    self.search(target-x, a+[x])
