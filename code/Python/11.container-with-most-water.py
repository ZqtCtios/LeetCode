class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea=0
        start=0
        end=len(height)-1
        while start<end:
            area=(end-start)*min(height[start],height[end])
            if area>maxarea:
                maxarea=area
            if height[start]< height[end]:
                start+=1
            else:
                end-=1
        return maxarea