"""
CISC365_PracticeProblems_Week4_Problem3:
Find the Majority Element
Written by: Prof. Ting Hu
"""

def find_majority(s,start,end):
    if start == end:
        return s[start]         
    else:
        mid = (end+start)//2
        l = find_majority(s, start, mid)
        r = find_majority(s, mid+1, end)
        if l == r:
            return l
        else:
            if s.count(l) > (end-start+1)/2:
                return l
            elif s.count(r) > (end-start+1)/2:
                return r
            else:
                return None
   
        
if __name__ =="__main__":  
    s = "abcbbab"
    print(find_majority(s,0,len(s)-1))

    s = "jklksj"
    print(find_majority(s,0,len(s)-1))
   
    s = "a"
    print(find_majority(s,0,len(s)-1))
    


    
