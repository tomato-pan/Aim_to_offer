class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic = {}  # 记录数字个数
        list1 = [] # 记录剩余需要计算的索引下标
        bulls = 0
        cows = 0
        for i in secret:
            dic[i] = secret.count(i)
        for k in range(len(secret)):
            if secret[k] == guess[k]:
                dic[guess[k]] -= 1
                bulls += 1
            else: # 剩余计算奶牛的索引下标
                list1.append(k)
        for j in list1:
            if dic.__contains__(guess[j]) and dic[guess[j]] > 0:
                dic[guess[j]] -= 1
                cows += 1
        return "{}A{}B".format(bulls, cows)

    def getHint1(self, secret: str, guess: str) -> str:
        pass


if __name__ == '__main__':
    s = Solution()
    print(s.getHint("1807", "7810"))
    print(s.getHint("1123", "0111"))
    print(s.getHint("1122", "1222"))
    print(s.getHint("1112", "1211"))
