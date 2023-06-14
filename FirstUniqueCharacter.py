class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for i in s:
            if i not in count:
                    count[i]=1
            else:
                   count[i]+=1
        for k in count:
            if count[k]==1:
                return s.index(k)
        return -1