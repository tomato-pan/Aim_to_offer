class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sign = {")":"(", "]":"[" , "}":"{"}
        for i in s:
            if stack and i in sign:
                if stack[-1] == sign[i]:stack.pop()
                else:return False
            else:
                stack.append(i)
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("{}{{}}"))
    print(s.isValid("{}({{}}"))
    print(s.isValid("()"))
