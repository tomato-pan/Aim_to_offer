class Solution:
    # 栈 牢记
    def removeDuplicates(self, S: str) -> str:
        list_s = []
        for i in range(len(S)):
            if list_s:
                if S[i] == list_s[-1]:
                    list_s.pop(-1)
                else:
                    list_s.append(S[i])
            else:
                list_s.append(S[i])
        return "".join(list_s)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates("aababaab"))
    print(s.removeDuplicates("abbaca"))
