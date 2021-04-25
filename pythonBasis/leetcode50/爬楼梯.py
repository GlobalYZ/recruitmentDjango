# 假设你正在爬楼梯。需要 n阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。
#
# 示例 1：
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
# 示例 2：
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# functools.lru_cache的作用主要是用来做缓存，他能把相对耗时的函数结果进行保存，避免传入相同的参数重复计算。
# 同时，缓存并不会无限增长，不用的缓存会被释放。
# functools.lru_cache(maxsize=128, typed=False)有两个可选参数，我们来看看他们分别代表的意义。
# * maxsize代表缓存的内存占用值，超过这个值之后，就的结果就会被释放，然后将新的计算结果进行缓存,其值应当设为2的幂 *
# * typed若为True，则会把不同的参数类型得到的结果分开保存 *
import functools

# 此题实为一个斐波那契实现fibonacci
class Solution:
    @functools.lru_cache()
    def climbStairs(self, n: int) -> int:
        return self.climbStairs(n-1) + self.climbStairs(n-2) if n > 2 else n

test = Solution()
result = test.climbStairs(4)
print(result)
