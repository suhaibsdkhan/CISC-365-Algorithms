is this fine, if not then refine it : base case (n=0) 
When there are no items the algo picks none 


IH: When n=k

When there are k items, the algo chooses the optimal solution
The solution by GreedyFKP has the maximum possible value that adds to the weight 

IP: when n=k+1

take A={p_1,p_2,p_3,...p_t} is the greedy algo choice 

take O={q_1,q_2,q_3,...q_r} is any choice 

1. First we show that p_1 is optimal and is included 

Suppose we say there is no optimal solution with p_1
O's first fraction is not p_1 so p_1>q_1, p1 has more value than q_1
we know total mass of A= total mass of o 
Since q_1<p_1, in O we take less amount of x_1, in O there has to be a x_i where q_i>p_i 

So let O*={p1,q2,q3...q'_i..q_k+1}

we know p_1>q_1 and q'_i<q_i  

We must make sure that the 

total_mass(O*)=case(p_i-q_i) * x_1.mass = (q_i-q'_i)*x_i.mass

We get that total_value(O*)-total_value(O)=(p_1-q1) * x_1.mass * ( (x_1.value/x_1.mass)-(x_i.value/x_i.mass))

which will be more than 0 so it is a contradiction and we know that O* has p_1 and is more optimal than O as the 
value difference is greater than 0.


2. We show that A is optimal

Since we have shown that p_1 is optimal and included. We know that the remaining problem includes k items left.

From the IH, GREEDYFKP is optimal on any set of k items.

The same set of k items remains after completing p_1. So since O* is optimal, the subset it uses for the rest of the problem
which is {p_1,p_3...p_k+1} is no better than the one that GreedyFKP picks, the solutions of O* and A will match therefore telling us A is also optimal.