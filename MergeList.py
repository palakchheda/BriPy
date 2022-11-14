class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2

        if l1.val <= l2.val:  # 1
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:  # 2
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    lis_1 = [1, 4, 9]
    lis_2 = [2, 4, 5, 10]
    m = Solution()
    print(m.mergeTwoLists(lis_1, lis_2))
