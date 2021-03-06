#LC338
"""
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]

示例 2:

输入: 5
输出: [0,1,1,2,1,2]

"""
class Solution:
    def countBits(self, num: int) -> list:
        bit_list=[]
        for i in range(num+1):
            bit_list.append(bin(i).count("1"))
        return bit_list
    # 动态规划
    def countBits1(self, num: int) ->list:
        bits = [0]
        highBit = 0
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                highBit = i
            bits.append(bits[i - highBit] + 1)
        return bits



if __name__ == '__main__':
    import time
    t1 =time.time()
    s = Solution()
    # s.countBits(10021321)
    # t2=time.time()
    # print(t2-t1)
    # s.countBits1(10021321)
    # print(time.time()-t2)
    print(100&99)