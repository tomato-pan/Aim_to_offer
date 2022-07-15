from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        min = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            cur = arr[i + 1] - arr[i]
            if cur < min:
                ans = []
                min = cur
            if cur == min:
                ans.append([arr[i], arr[i + 1]])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minimumAbsDifference([4, 2, 1, 3]))
