class Solution:
    def longestValidParentheses(self, s: str) -> int:

    	# lengtn = 0 -> no valid paenthesis
        if len(s)==0:
            return 0
        
        # point 1

        a=[[s[0],1,0]]
        
        for i in range(1,len(s)):
            if s[i]=='(':

            	#Point 2

                if a[-1][0]==s[i]: 

                	# Increase the value if valid pairs are 0    
                    if a[-1][2]==0:   
                        a[-1][1]+=1

                    # Create a new array if previously valid pair exists
                    else:
                        a.append([s[i],1,0])
                
                else:
                	#create new array if previous element was different
                    a.append(['(',1,0])
            
            # if ")" occurs
            else:
            	#increament if the previous element was the same
                if a[-1][0]==s[i]:
                    a[-1][1]+=1
                

                else:

                	# if "(" are avaliable , decreament the occurances of "(" and increse the number of valid pairs
                    if a[-1][1]>0:
                        a[-1][1]-=1
                        a[-1][2]+=1

                        # if two valid sequences are together, then merge those two sequences
                        if a[-1][1]==0:
                            if len(a)>1 and a[-2][0]=='(':
                                a[-2][2]+=a[-1][2]
                                a.pop()
                    else:
                        a.append([s[i],1,0])
        k=0

        # choose the longest sequence found
        for i in range(len(a)):
            if a[i][2]>k:
                k=a[i][2]
        return k*2