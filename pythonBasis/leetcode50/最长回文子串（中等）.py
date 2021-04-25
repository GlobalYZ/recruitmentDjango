# 给你一个字符串 s，找到 s 中最长的回文子串。
# 示例 1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。

# 示例 2：
# 输入：s = "cbbd"
# 输出："bb"

# 示例 3：
# 输入：s = "a"
# 输出："a"

# 示例 4：
# 输入：s = "ac"
# 输出："a"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # n = len(s)
        # if n == 1:
        #     return s
        # elif n == 2:
        #     return
        # 如果字符串长度小于2或者s等于它的倒序，则直接返回s
        if len(s) < 2 or s == s[::-1]:
            return s
        n = len(s)
        # 定义起始索引和最大回文串长度，odd奇，even偶
        start, maxlen = 0, 1
        # 因为i=0的话必然是不可能会有超过maxlen情况出现，所以直接从1开始
        for i in range(1, n):
            # 取i及i前面的maxlen+2个字符
            odd = s[i - maxlen - 1:i + 1]  # len(odd)=maxlen+2
            # 取i及i前面的maxlen+1个字符
            even = s[i - maxlen:i + 1]  # len(even)=maxlen+1
            if i - maxlen - 1 >= 0 and odd == odd[::-1]:
                start = i - maxlen - 1
                maxlen += 2
                continue
            if i - maxlen >= 0 and even == even[::-1]:
                start = i - maxlen
                maxlen += 1
        return s[start:start + maxlen]

test = Solution()
# print(test.longestPalindrome("ac"))
print(test.longestPalindrome("dsaasq"))
