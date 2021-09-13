class Solution:
    def lengthOfLongestSubstring(self,s:str)->int:
        max1 = 0
        left = 0
        map = dict()
        for i in range(len(s)):
            if map.__contains__(s[i]):
                left = max(left,map.get(i)+1)
            map[s[i]]=i
            max1 = max(max1,i-left+1)
        return max1
