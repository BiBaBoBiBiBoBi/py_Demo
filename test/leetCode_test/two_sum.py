from typing import Optional, List


class Solution:
    # 给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。
    # 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。你可以按任意顺序返回答案。
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in dic:
                return [dic[diff],i]
            dic[num]=i
        return []


    def twoSum2(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            diff = target - nums[i]
            try:
                index = nums.index(diff)
            except ValueError:
                print(f"{diff} 不在列表中")
                continue
            if index == i :
                continue
            return [i,index]

    def bubble_sort(self,nums:List[int]) :
        n = len(nums)
        for i in range(n):
            if_moved=False
            for j in range(n-i-1):
                if nums[j]<nums[j+1]:
                    if_moved=True
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            if not if_moved:
                break

    # 必须nums为有序数组，一般是升序
    def binary_search(nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left<=right:
            mid = left+ (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left = mid +1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    solution =  Solution()
    lst = [3,6,1,2,9]
    solution.bubble_sort(lst)
    print(lst)
