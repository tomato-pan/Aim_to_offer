from typing import List
import collections


class Solution:
    # 直接法
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = []
        for i in range(len(nums)):
            if i + k - 1 == len(nums):
                break
            else:
                max_list.append(max(nums[i:i + k]))
        return max_list

    # 2只算一次最大，然后滑动比较,本次方法忘记清空窗口滑动后丢失的元素，应使用单调队列

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        # if not nums:return []
        # if k==1:return nums
        # max_nums = max(nums[0:k])
        # max_list = [max_nums]
        # for i in range(1,len(nums)):
        #     if i+k-1==len(nums): break
        #     else:
        #         if nums[i+k-1]>max_nums:
        #             max_nums=nums[i+k-1]
        #             max_list.append(max_nums)
        #         else:
        #             max_list.append(max_nums)
        # return max_list
        if not nums or k == 0: return []
        deque = collections.deque()
        # 未进入窗口时
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        # 形成窗口滑动后
        for i in range(k, len(nums)):
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow(nums=[1, -1], k=3))
    print(s.maxSlidingWindow2(nums=[1, -1], k=1))
