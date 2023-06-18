class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a=set("qwertyuiop")
        b=set("asdfghjkl")
        c=set("zxcvbnm")
        lst=[]
        for i in words:
            t=set(i.lower())
            if t&a==t:
                lst.append(i)
            elif(t&b==t):
                lst.append(i)
            elif(t&c==t):
                lst.append(i)
        return lst        
        