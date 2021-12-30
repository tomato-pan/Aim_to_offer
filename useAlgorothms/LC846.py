from typing import List, Counter

"""
Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。
给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true ；否则，返回 false 
示例 1：
输入：hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
输出：true
解释：Alice 手中的牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
示例 2：
输入：hand = [1,2,3,4,5], groupSize = 4
输出：false
解释：Alice 手中的牌无法被重新排列成几个大小为 4 的组。

"""


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False
        cnt = Counter(hand)
        while cnt:
            key = min(cnt.keys())
            for i in range(groupSize):
                if key+i in cnt:
                    if cnt[key+i]==1:
                        del cnt[key+i]
                    else:
                        cnt[key + i] -= 1
                else: return False
        return True


        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isNStraightHand(hand=[1, 2, 3, 4, 5], groupSize=4))
    print(s.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3))
