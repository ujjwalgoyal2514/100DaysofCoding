################# BRUTE FORCE #########################################
# O(n)
"""
def anagram(a,b):
    a=a.replace(" ","").lower()
    b=b.replace(" ","").lower()
    return sorted(a) == sorted(b)


print(anagram('dog','God')    )    
"""

#################### ANOTHER CODE Without Using sorted Function###################

def anagram(a,b):
    a=a.replace(" ","").lower()
    b=b.replace(" ","").lower()
    count={}
    if(len(a)!=len(b)):
        return False
    for letter in a:
        if(letter in count):
            count[letter]+=1
        else:
            count[letter]=1
    for letter1 in b:
        if(letter1 in count):
            count[letter1]-=1
        else:
            count[letter1]=1
    for k in count:
        if(count[k]==0):
            return True
    return False          


print(anagram('dogr','God')) 