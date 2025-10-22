# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # 二分查找,查找目标元素 下表，nums有序
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                pass
                right = mid - 1
            elif target > nums[mid]:
                pass
                left = mid + 1
            else:
                return mid
        return -1

    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        def reverse_listNode(head: ListNode) -> ListNode:
            if not head:
                return head
            pre, cur = None, head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

        lst1 = reverse_listNode(l1)
        lst2 = reverse_listNode(l2)
        dummy = ListNode(-1)
        cur = dummy
        carry = 0
        while lst1 or lst2:
            sum = 0
            if lst1:
                sum += lst1.val
                lst1 = lst1.next
            if lst2:
                sum += lst2.val
                lst2 = lst2.next
            sum += carry
            num = sum % 10
            carry = sum // 10
            cur.next = ListNode(num)
            cur = cur.next
        if carry!=0:
            cur.next = ListNode(carry)

        return reverse_listNode(dummy.next)