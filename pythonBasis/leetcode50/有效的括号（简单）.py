# 给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
# 示例 1：
# 输入：s = "()"
# 输出：true
#
# 示例2：
# 输入：s = "()[]{}"
# 输出：true
#
# 示例3：
# 输入：s = "(]"
# 输出：false
#
# 示例4：
# 输入：s = "([)]"
# 输出：false
#
# 示例5：
# 输入：s = "{[]}"
# 输出：true
class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")# replace的变换，如果没有需要更换的，则会返回原字符串
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        return s == ""

test = Solution()
print(test.isValid("([{}])"))
testReplace = "222"
testReplace = testReplace.replace("{","")
print(testReplace)