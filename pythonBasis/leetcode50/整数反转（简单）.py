# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围[−2**31,2**31− 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 示例 1：
#
# 输入：x = 123
# 输出：321
#
# 示例 2：
# 输入：x = -123
# 输出：-321
#
# 示例 3：
# 输入：x = 120
# 输出：21
#
# 示例 4：
# 输入：x = 0
# 输出：0
import sys


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            s = str(x)
            s = s[::-1]
            return 0 if int(s) > 2 ** 31 - 1 else int(s)
        else:
            s = str(-x)
            s = s[::-1]
            return 0 if int(f'-{s}') < -2 ** 31else int(f'-{s}')


test = Solution()
intTest = test.reverse(123)
print(2 ** 31 - 1)
print(-2 ** 31)
print(-sys.maxsize - 1)
print(type(intTest))
print(intTest)
1534236469
2147483647