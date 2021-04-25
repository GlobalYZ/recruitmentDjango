# 给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
# 初始化nums1 和 nums2 的元素数量分别为m 和 n 。你可以假设nums1 的空间大小等于m + n，这样它就有足够的空间保存来自 nums2 的元素。
#
# 示例 1：
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
#
# 示例 2：
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        不要返回任何，就地修改nums1
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m,m + n):
            nums1[i] = nums2[j]
            j = j + 1
        nums1.sort()
        print(nums1)
print("")
test = Solution()
test.merge([1,3,2,0,0,0,0],3,[2,2,3,7],4)