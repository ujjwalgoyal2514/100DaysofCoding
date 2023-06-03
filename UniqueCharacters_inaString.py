def unique(a):
    if(len(a)==0):
        return False
    if len(a)==1:
        return True
    count={}
    for i in a:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
            
    for k in count:
        if count[k]>1:
            return False
    return True                


d=unique('d')
print(d)
