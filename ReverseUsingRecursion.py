# How can a given string be reversed using recursion?
def reverse(a):
    l=len(a)
    if len(a)==1:
       return a
    else:
        return a[-1]+reverse(a[0:l-1])
    
    
print(reverse("swiss") )   