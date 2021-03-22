class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:]+s[:n]

if __name__ == '__main__':
    s = Solution()
    print(s.reverseLeftWords(s = "abcdefg", n = 2))
    print(s.reverseLeftWords(s = "lrloseumgh", n = 6))