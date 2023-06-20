class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        count={}
        for i in candyType:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        l=len(candyType)//2
        l1=len(count)
        if(l1==l):
            return l
        elif(l1>l):
            return l
        elif(l1==1):
            return l1
        else:
            return l1
        
            
            