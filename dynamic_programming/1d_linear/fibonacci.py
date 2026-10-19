def fib_dp(n):

    if n<=1:
        return n        #return the base case for 1 and 0

    F=[0]*(n+1)
    F[0]=0                  #set initial numbers
    F[1]=1
    for i in range(2,n+1):                #generate dynamically and save in F
        F[i]=F[i-2]+F[i-1]

    return F[n]


#recursive, O(2^n) since it recomputes the same values

def fib_recursive(n):

    if n<=1:
        return n
    else:
        return fib_recursive(n-2)+fib_recursive(n-1)


if __name__ == "__main__":
    print(fib_dp(10), fib_recursive(10))    # 55 55
    print(fib_dp(90))                       # instant, the recursive one would never finish
