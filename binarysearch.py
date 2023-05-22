# algorithm for binary search

'''
we take out the index of middle element
we check for element at middle index== query if yes element found
if not we check query is bigger than element or smaller
if bigger we elemenate the left side and search element on right one by one 
if smaller we eliminate right and check elements on left one by one '''

# we check if list is empty or element not found
# this is case of ascending


# Time Complexity is O(log n) Space complexity is O(1)
# the card is sorted in descending order 
# test_location is taken in terms of only descending otherwise apply just binary srarching
def test_location(card,query,mid):
    if card[mid]==query:
        if mid-1>=0 and card[mid-1]==query:
            return 'left'
        else:
            return 'found'
    elif card[mid] <query:
        return 'left'   
    elif card[mid]>query:
        return 'right'
    
def locate_cards(card,query):  
    min=0
    max=len(card)-1

    while min<=max:
        middle=(min+max)//2
        print("middle=", middle)
        result=test_location(card,query,middle)
        if(result=='found'):
            return middle
        elif(result=='right'):
            min=middle+1
        elif(result=='left'):
            max=middle-1       
    return(-1)   


print(locate_cards([8, 8,6, 6, 6, 3, 2, 2, 2, 0, 0, 0],6))

