Base case: 
When k=200

The algo will pick a toonie which is optimal

Inductive hypothesis:

For some integer k>=200, MinCoinChange returns an optimal solution for every target value up to k by using minimum number of coins possible


Inductive Step:;

We WTS that it returns optimal solution for target= k+1

A={a1,a2,....,at} is MinCoinChange's solution for k+1

O={o1,o2,.....or} is any optimal solution

1. Optimal solution with a toonie or a1

If O already has a toonie then we are done, it is the most optimal

if O doesnt have a toonie 

O is a set of coins summing to K+1 >=200. must be a subset in O whose sum is at least 200

Exchanging 200 for a toonie reduces the number of coins 

Therefore it is an optimal sollution 

2. Showing that A is optimal

We know that optimal with toonie exists so that is O*={200,x2,x3,...}

Both A and O* start with 200
so remainder is r=(k+1)-200

Now that r<=k we know that by iH, MinCOinChanges solution for any target <=k is already optimal.

So |Ar|=|O*|

So thus |A|=1+|Ar| = 1+|O*R| = |O*|

Thus they use the same number of coins and are optimal. 
