# 给你一个有序数组nums ，请你原地删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。不要使用额外的数组空间，你必须在
# 原地修改输入数组并在使用O(1)额外空间的条件下完成。
# 说明:
# 为什么返回数值是整数，但输出的答案是数组呢?
# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
# 你可以想象内部操作如下:
#
#     // nums
#     是以“引用”方式传递的。也就是说，不对实参做任何拷贝
#     int
#     len = removeDuplicates(nums);
#
#     // 在函数里修改输入数组对于调用者是可见的。
#     // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
#     for (int i = 0; i < len; i++) {
#         print(nums[i]);
#     }
# 示例1：
# 输入：nums = [1, 1, 2]
# 输出：2, nums = [1, 2]
# 解释：函数应该返回新的长度2 ，并且原数组nums
# 的前两个元素被修改为1, 2 。不需要考虑数组中超出新长度后面的元素。
#
# 示例2：
# 输入：nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# 输出：5, nums = [0, 1, 2, 3, 4]
# 解释：函数应该返回新的长度5 ， 并且原数组nums的前五个元素被修改为0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
from typing import List


class Solution:
    # 此题因为数组是正序排列的，所以只需要依次对比下一个数就好
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                del nums[i + 1]
            else:
                i = i + 1

        return len(nums)

test = Solution()
l = [1,2,2,3,3,3,6,6,7,8]
n = test.removeDuplicates(l)
print(n)