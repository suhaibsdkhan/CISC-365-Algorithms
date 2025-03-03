Proof Road-trip by induction 



Base: if n=1, we can see if we can make it to NYC on a single tank of gas

IH: Assume the algo RoadTrip find an optimal solution when we have a full tank of gas and there are k stations 
ahead of us so k>=1

IP: 

We need to show that RoadTrip can find an optimal solution when we have a full tank of gas and 
k+1 stations are ahead of us .

Lets take road trips solution as A={a1,a2,a3,....at}

1. There exists at least one optimal solution that starts with our greedy algos first choice a1

Take any optimal O={o1,o2,o3,...or}

o1 comes before a1 because a1 is the farthest we can reach with our tank of gas chosen by our greedy algo

o1<=a1

We can reach o2 after reaching a1 as we can reach o2 after reaching o1

Now take O*={a1,o2,o3,....or} and say it is optimal since |O*|=|O|

2. Rest of the greedy algos solution A {a2,a3,...at} is optimal for the reduced problem
We now have k stations since a1 is done. By Inductive Hypothesis(IH) when there is k stations, our greedy algo can find an optimal solution 

3. Combine the 1 and 2 and get an optimal solution to the original problem.

|A| <= |O*| so A is an optimal solution.