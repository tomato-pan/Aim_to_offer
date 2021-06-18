'''
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
输入：s = "cbbd"
输出："bb"
'''
import time

# 返回回文子串，不是子序列
class Solution:
    #暴力解法
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:return s
        start = 0
        end = 0
        max_len = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)+1):
                # 判断回文
                if s[i:j]==s[i:j][::-1]:
                    if max_len<max(max_len,j-i):
                        start=i
                        end=j
                        max_len = max(max_len,end-start)
        return s[start:end]
    # dp 判断上一层关系是否为回文字符串-->转移方程
    def longestPalindrome1(self, s: str) -> str:
        size = len(s)
        # 特殊处理
        if size == 1:
            return s
        # 创建动态规划dynamic programing表
        dp = [[False for _ in range(size)] for _ in range(size)]
        # 初始长度为1，这样万一不存在回文，就返回第一个值（初始条件设置的时候一定要考虑输出）
        max_len = 1
        start = 0
        for j in range(1, size):
            for i in range(j):
                # 边界条件：
                # 只要头尾相等（s[i]==s[j]）就能返回True
                if j - i <= 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        cur_len = j - i + 1
                # 状态转移方程
                # 当前dp[i][j]状态：头尾相等（s[i]==s[j]）
                # 过去dp[i][j]状态：去掉头尾之后还是一个回文（dp[i+1][j-1] is True）
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        cur_len = j - i + 1
                # 出现回文更新输出
                if dp[i][j]:
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i

        return s[start:start + max_len]


if __name__ == '__main__':
    t1 = time.time()
    aa = "ibawpzhrunsgfobmenlqlxnprtgijgbeicsuoihnmcekzmvtffmlpzuwlimuuzjhkzppmpqqrfwyrjrsltkypjpcjffpvhtdiwjdonutobpecsiqubiusvwsyhrddqjeqqpgofifmwvmcdjixjvjxrvyabqaqumfqiiqxizmhzevhxutsbgzcfggyyvolwaxfcpjhfpksxvgyxhddcssnxhygzvmyxrxqizzhpluxkautjmieximoskcffimctsfzgmihtoxkltopwobtfjvjymtuknxmsgevkeklprcaudidywwkfuhtatpeeiewczpwiegmpjquayfleczrvzekikbaeocpcurtxhcsysbbsyschxtrucpcoeabkikezvrzcelfyauqjpmgeiwpzcweieeptathufkwwydiduacrplkekvegsmxnkutmyjvjftbowpotlkxothimgzfstcmiffcksomixeimjtuakxulphzziqxrxymvzgyhxnsscddhxygvxskpfhjpcfxawlovyyggfczgbstuxhvezhmzixqiiqfmuqaqbayvrxjvjxijdcmvwmfifogpqqejqddrhyswvsuibuqiscepbotunodjwidthvpffjcpjpyktlsrjrywfrqqpmppzkhjzuumilwuzplmfftvmzkecmnhiousciebgjigtrpnxlqlnembofgsnurhzpwabi"
    s = Solution()
    print(s.longestPalindrome(aa))
    t2 = time.time()
    print(t2-t1)
    print(s.longestPalindrome1(aa))
    print(time.time()-t2)
    print(s.longestPalindrome(aa)==s.longestPalindrome1(aa))