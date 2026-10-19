Proof activity selection


Base case(n==1):

if there is only one activity then it is returned as it is the only one that can be done 



IH:

If there are k activities then Activity selection chooses the optimal number of activities from k


IP:

Now if we have k+1 acitivties

A={a1,a2,a3,...at} is the set choosen by greedy

O={o1,o2,....or} is any set possible 

We need to show that |A|>=|O|

1. We first show that a1 is optimal

Since we know that a1 is the earliest and most optimal so we know a1.start_time is before o1.start_time
Therefore we know that a1 is also done before o2 as o1 happened before o2
Since a1 is more optimal that o1 we can add it to new set O*

O*={a1,o2,o3,...or}

Since it does not break feasability, we know it is more optimal than O 

2. We show that the A is optimal

Since greedy first works on a1 then the reduced problem, we know that by IH, now that we have 
k activities, the greedy algo will find a solution to the reduced problem . Where O* will have a2,a3 if they are more optimal and possible.



Thus we will get |A|>=|O| which proves that greedy can find optimal with A.

