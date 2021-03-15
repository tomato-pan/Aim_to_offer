class Solution:
    def calculate(self, s: str) -> int:
        # 入栈 stack.append() 出栈 stack.pop()
        ops = [1]
        sign = 1
        res = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    # 10以上的数字
                    num = num*10 + ord(s[i]) - ord('0')
                    i += 1
                res += num * sign
        return res

if __name__ == '__main__':
    import time
    s = Solution()
    print(s.calculate("1+3+(4-3)+13"))
