# LC354
'''
输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
'''


class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        if not envelopes: return 0
        n = len(envelopes)
        for k in range(n):
            if envelopes[k][0]>envelopes[k][1]:
                envelopes[k][0],envelopes[k][1]=envelopes[k][1],envelopes[k][0]
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        left: int = envelopes[0][0]
        right: int = envelopes[0][1]
        res: int = 0  # 覆盖区间个数，即被删除区间个数
        for i in range(1, n):
            list_intv = envelopes[i]
            # 情况1找到覆盖区间
            if (left <= list_intv[0] and right >= list_intv[1]):
                res += 1
            # 情况2找到相交区间,跳过
            if (left <= list_intv[0] and right <= list_intv[1]):
                right = list_intv[1]
            if right < list_intv[0]:
                left = list_intv[0]
                right = list_intv[1]
        print(n-(res+1))
        return n-(res+1)
    def maxEnvelopes1(self, envelopes) -> int:
        if not envelopes: return 0
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                print(i,j)
                if envelopes[j][1]<envelopes[i][1]:
                    dp[i] = max(dp[i],dp[j]+1)
                print(dp)
        print(dp)
        return max(dp)
if __name__ == '__main__':
    e1 = [[5,4],[6,4],[6,7],[2,3]]
    envelopes = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
    ss = Solution()
    print(ss.maxEnvelopes1(envelopes))
