from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)
if __name__ == '__main__':
    s = Solution()
    print(s.distributeCandies([1, 1, 2, 2, 3, 3]))
    print(s.distributeCandies([1, 1, 2, 3]))