# How do you print the first non-repeated character from a string?
def repeat(s):
    count={}
    for i in s:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for k in count:
        if count[k]<2:
            print(k)
            break
    
    
    
repeat("hello")                