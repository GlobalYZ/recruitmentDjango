# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 示例 1：
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#
# 示例 2：
# 输入：l1 = [], l2 = []
# 输出：[]
#
# 示例 3：
# 输入：l1 = [], l2 = [0]
# 输出：[0]
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNode_handle():
    def __init__(self):
        self.cur_node = None

    # 查找
    def find(self, node, num, a=0):
        while node:
            if a == num:
                return node
            a += 1
            node = node.next

    # 增加
    def add(self, data):
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    # 打印
    def printNode(self, node):
        while node:
            print('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
            node = node.next

    # 删除
    def delete(self, node, num, b=1):
        if num == 0:
            node = node.next
            return node
        while node and node.next:
            if num == b:
                node.next = node.next.next
            b += 1
            node = node.next
        return node

    # 反转
    def reverse(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        result = ListNode()
        result_handle = ListNode_handle()
        for i in list:
            result = result_handle.add(i)
        return result


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(None)
        node = res# node = res 的作用是将一个哑节点作为头节点，最后返回哑节点的next
        while l1 and l2:
            if l1.val < l2.val:
                node.next, l1 = l1, l1.next# 元组的解包，等同于node.next=l1 ; l1=l1.next
            else:
                node.next, l2 = l2, l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return res.next


listN1 = ListNode()
listN_h1 = ListNode_handle()
list_test1 = [1, 3, 8]
# for i in list_test1:
#     listN = ListN_h.add(i)
# 我发现单独定义这个操作类，如果对一个ListNode操作还好，中途如果穿插ADD了另一个ListNode对象，地址同样会指向前一个的ADD值
listN1 = listN_h1.add(1)
# listN2 = ListN_h.add(2)# 这个listN2就是穿插
listN1 = listN_h1.add(3)
listN1 = listN_h1.add(8)
# ListN_h.printNode(listN)
listN1 = listN_h1.reverse(listN1)
listN_h1.printNode(listN1)



listN2 = ListNode()
listN_h2 = ListNode_handle()
list_test2 = [2, 4, 6]
for i in list_test2:
    listN2 = listN_h2.add(i)
listN2 = listN_h2.reverse(listN2)
listN_h2.printNode(listN2)

print("-------------------------以下是测试这道题的代码-----------------------------")
test = Solution()
listN3 = test.mergeTwoLists(listN1,listN2)

listN_h2.printNode(listN3)

print(listN1.val,listN1.next.val)