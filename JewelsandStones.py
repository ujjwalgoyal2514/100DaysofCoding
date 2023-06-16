class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        f=0
        lst=[]
        s=0
        for j in stones:
            if j in jewels:
                f+=1
        # for k in count:
        #     lst.append(count[k])
        # for i in lst:
        #     s=s+i
        return f  