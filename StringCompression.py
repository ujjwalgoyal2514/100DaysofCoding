# input AAAABBBBCCCCC
#output  A4B4C5

def compresss(a):
    count={}
    lst=[]
    if(len(a)==0):
        return 0
    elif(len(a)==1):
        return a[0]+str(1)
    for i in a:
         if(i in count):
                count[i]+=1
         else:
                count[i]=1   
                
    for k in count:
        lst.append(k)
        lst.append(str(count[k]))   
        
    return "".join(lst)     


s=compresss("Aaaaaaaa") 
print(s)                