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
        if num<0:return []
        elif num==0:return [0]
        else:
            for i in range(0,num+1):
                i = str(bin(i))
                bit_list.append(i.count("1"))
        print(bit_list)
        return bit_list

if __name__ == '__main__':
    s = Solution()
    s.countBits(5)