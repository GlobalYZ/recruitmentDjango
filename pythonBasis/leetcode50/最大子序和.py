# 给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组[4,-1,2,1] 的和最大，为6 。
#
# 示例 2：
# 输入：nums = [1]
# 输出：1
#
# 示例 3：
# 输入：nums = [0]
# 输出：0
#
# 示例 4：
# 输入：nums = [-1]
# 输出：-1
#
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        可以理解为思想是动态规划，nums[i-1]并不是数组前一项的意思，而是到前一项为止的最大子序和，和0比较是因为只要大于0，
        就可以相加构造最大子序和。如果小于0则相加为0，nums[i]=nums[i]，相当于最大子序和又重新计算。其实是一边遍历一边计算最大序和
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
test = Solution()
print(test.maxSubArray(nums))