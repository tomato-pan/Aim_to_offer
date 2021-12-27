from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        length = len(ages)
        count, i, j = 0, 0, 0
        for k in range(length):
            print(i,j)
            while (i < k and not self.check(ages[i], ages[k])): i += 1
            if j < k: j = k
            while (j < length and self.check(ages[j], ages[k])): j += 1
            if j > i: count += j - i - 1
        return count

    def check(self, x, y):
        if y <= 0.5 * x + 7: return False
        if y > x: return False
        if y > 100 and x < 100: return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.numFriendRequests([101, 56, 69, 48, 30]))
