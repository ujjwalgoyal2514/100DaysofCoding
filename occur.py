def occur(a,c):
    a=a.replace(" ","")
    count={}
    for i in a:
        if i  in count:
            count[i]+=1
        else:
             count[i]=1
    for k in count:
        if k==c:
            return count[k]   
        
        
print(occur('Today is Monday','a') )                