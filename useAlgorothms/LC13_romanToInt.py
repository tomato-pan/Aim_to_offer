class Solution:
    def romanToInt(self, s: str) -> int:
        dic =  {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90,  'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        res = 0
        i = 0
        while i<len(s):
            str1 = s[i:i+2]
            if str1 in dic:
                res += dic[str1]
                i+=2
            else:
                res +=dic[s[i]]
                i+=1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("CDI"))