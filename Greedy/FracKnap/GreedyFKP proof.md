is this fine, if not then refine it : base case (n=0) 
When there are no items the algo picks none 


IH: When n=k

When there are k items, the algo chooses the optimal solution
The solution by GreedyFKP has the maximum possible value that adds to the weight 

IP: when n=k+1

take A={p_1,p_2,p_3,...p_t} is the greedy algo choice 

take O={q_1,q_2,q_3,...q_r} is any choice 

1. First we show that p_1 is optimal and is included 

suppose we say there is no optimal solution with p_1. 
We know that O's first fraction is not p_1 so p_1 is greater than q1

we also know that the total mass of A and O are the same and is c

since we are taking a smaller fraction of x_1 in O, there must be another x_i that q_i is taking more than A is taking with p_i
we know that there is a difference p_1-q_1 * x1.mass

Now lets make O* where O*={p_1,q_2,q_3....,q_(k+1)}  where we HAVE taken p_1
here we know that since we took p_1, there is a q'i that is lesser than q_i so we have 
q-q'i * xi.mass  so that mass(O*) is c

so we write that p_1-q_1 * x_1.mass = q-q'i * x_i.mass (equation 1)
we also write Total_value(O*)-total_value(O) = p_1-q_1 * x_1.value = q-q'i * x_i.value (equation 2)
then we substitute in q-q'i from equation 1 into equation 2 to simplify and get 
Total_value(O*)-total_value(O) > 0   (greater than 0)
This contradicts our assumption that firstly there is no optimal solution with p_1 and secondly O* has a larger value than O so O is not optimal and 
O* is .

2. We show that A is optimal

Since we have shown that p_1 is optimal and included. We know that the remaining problem includes k items left.

From the IH, GREEDYFKP is optimal on any set of k items.

The same set of k items remains after completing p_1. So since O* is optimal, the subset it uses for the rest of the problem
which is {p_1,p_3...p_k+1} is no better than the one that GreedyFKP picks, the solutions of O* and A will match therefore telling us A is also optimal.