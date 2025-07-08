'''
字符串：3，49，30
线性表：86，16，27，732
队列：641，406，899
栈：946，116，117，895
哈希表：61，729，25，554
dfs：105，112，98，494，547，1254
bfs：1091，1129，102，101，752
'''
from typing import Optional


def bracket_is_pair(s):
    pass
    store_lst = []
    for i in s:
        if store_lst:
            last = store_lst[-1]
            if is_pair(last, i):
                store_lst.pop()
                continue
        store_lst.append(i)
    return not store_lst


def is_pair(last, cur):
    if last == "(" and cur == ")" or last == "{" and cur == "}" or last == "[" and cur == "]":
        return True
    return False


'''Given a string s, find the length of the longest substring without duplicate characters.'''


# 3
def lengthOfLongestSubstring(s):
    left = max_len = 0
    char_set = set()
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len


# 704
def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:  # 修改为 <=，确保搜索区间包含 l == r 的情况
        mid = l + (r - l) // 2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return -1


# 27 double-indicator
def removeElement(nums, val):
    slow, length = 0, len(nums)
    for fast in range(length):
        if nums[fast] == val:
            continue
        nums[slow] = nums[fast]
        slow += 1
    print(f"nums = {nums}")
    return slow


# 977
def sortedSquares(nums):
    nums = list(map(lambda x: x * x, nums))
    nums = sorted(nums)
    print(f"nums ={nums}")
    return nums


def sortedSquares_double_indicator(nums):
    length_nums = len(nums)
    l, r = 0, length_nums - 1
    res_lst = [0 for _ in range(length_nums)]
    res_tail = len(res_lst) - 1
    while res_tail >= 0:
        if nums[l] ** 2 >= nums[r] ** 2:
            res_lst[res_tail] = nums[l] ** 2
            l += 1
        else:
            res_lst[res_tail] = nums[r] ** 2
            r -= 1
        res_tail -= 1
    print(f"res_lst ={res_lst}")
    return res_lst


# 209 slide-window
def minSubArrayLen(target, nums):
    leng = len(nums)
    if leng == 0: return 0
    l, r, cur_sum, sub_len = 0, 0, 0, -1
    while r < leng:
        cur_sum += nums[r]
        if cur_sum >= target:
            sub_len = r - l + 1 if sub_len == -1 else min(sub_len, r - l + 1)
            cur_sum -= nums[l]
            l += 1
        r += 1
    return sub_len if sub_len != -1 else 0


# 59
def generateMatrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1
    while top <= bottom and left <= right:
        # top
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        # right
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        '''下，上/左，右 的重合判定'''
        # bottom
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
        # left
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    return matrix


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 203
def removeElements(head: Optional[ListNode], target):
    dummy = ListNode(0, head)
    curr = dummy
    # 在访问 curr.next.val 之前，需要检查 curr.next 是否为 None。如果 curr.next 是 None，访问 curr.next.val 会导致程序崩溃。
    while curr and curr.next:
        if curr.next.val == target:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next


# 707
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
class MyLinkedList:
    # Initializes the MyLinkedList object.
    def __init__(self):
        self.head = None
        self.size = 0

    # Get the value of the index-th node in the linked list. If the index is invalid, return -1.
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(0, index):
            current = current.next
        return current.val

    # Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    def addAtHead(self, val: int) -> None:
        # o = ListNode(val)
        # o.next = self.head
        # self.head = o
        self.addAtIndex(0,val)

    # Append a node of value val as the last element of the linked list.
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        current = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1


if __name__ == '__main__':
    s = "(([]){})[]"
    # print(bracket_is_pair(s))
    # print(lengthOfLongestSubstring("pwwkew"))
    # print(binary_search([-1, 0, 3, 5, 9, 12], 9))
    # print(binary_search([5], 5))
    # print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
    # print(sortedSquares_double_indicator([-7, -3, 2, 3, 11]))
    # print(minSubArrayLen(6, [10, 2, 3]))
