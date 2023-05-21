def pair__sum(arr,b):
    if(len(arr)<2):
        return 'array less than 2'
    
    seen=set()
    output=set()    
    for num in arr:
        target=num-b
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(target,num)),(max(target,num))))
    print (' '.join(map(str,list(output)))  )         

                       
pair__sum([1,3,2,2],6)       
    