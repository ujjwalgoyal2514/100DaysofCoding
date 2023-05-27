class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       s=s.strip(" ")
       s=s.split(" ")
       b=len(s)-1
       c=len(s[b])
       return c