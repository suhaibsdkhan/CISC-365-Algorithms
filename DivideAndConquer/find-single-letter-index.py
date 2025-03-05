"""
CISC365_PracticeProblems_Week4_Problem1:
Find the Single Letter
Written by: Prof. Ting Hu
"""


def find_single(s,start,end):
    if start>end:  # two pointers cross  
        return None
    elif start == end:
        return start         
    else:  # binary search
        mid = (end+start)//2
    
        if mid%2==0: # mid is even
            if s[mid]==s[mid+1]: # the single letter is in the second half
                return find_single(s,mid+2,end)
            else:
                return find_single(s,start,mid)
        else: # mid is odd
            if s[mid]==s[mid-1]: # the single letter is in the second half
                return find_single(s,mid+1,end)
            else:
                return find_single(s,start,mid-1)

        
if __name__ =="__main__":
    s = "aadbb"
    print(find_single(s,0,len(s)-1))

    s = "cckkaadbbggii"
    print(find_single(s,0,len(s)-1))

    s = "b"
    print(find_single(s,0,len(s)-1))

    s = "aaccdd"
    print(find_single(s,0,len(s)-1))

    s = "aaccddb"
    print(find_single(s,0,len(s)-1))

    s = "aabccddee"
    print(find_single(s,0,len(s)-1))

    s = "aaccddxjj"
    print(find_single(s,0,len(s)-1))
