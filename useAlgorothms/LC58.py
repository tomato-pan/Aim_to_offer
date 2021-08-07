class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(' ')
        print(x)
        for i in x[::-1]:
            if i != '':
                return len(i)
        return 0



if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord("Hello World aaa"))
    print(s.lengthOfLastWord("Hello "))
    print(s.lengthOfLastWord(" "))
    print(s.lengthOfLastWord(" a"))
    print(s.lengthOfLastWord("a"))
    print(s.lengthOfLastWord("a "))
    print(s.lengthOfLastWord("aaaaa"))
