# O(m+n)合并数组
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newList = []
        n1 = len(nums1)
        n2 = len(nums2)
        r1 = r2 = 0
        while r1 < n1 and r2 < n2:
            if nums1[r1] < nums2[r2]:
                newList.append(nums1[r1])
                r1 += 1
            else:
                newList.append(nums2[r2])
                r2 += 1
        newList = newList+nums1[r1:]+nums2[r2:]
        n = len(newList)
        if n % 2 == 1:
            return newList[n//2]
        else:
            return (newList[n//2]+newList[n//2-1])/2
