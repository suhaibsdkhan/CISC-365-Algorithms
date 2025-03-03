# Proof of Optimality for GreedyFKP via Induction

We want to prove that the **GreedyFKP** algorithm finds an **optimal** solution (i.e., a solution with maximum total value) for the fractional knapsack problem. Below is a detailed inductive proof.

---

## Base Case: \(n = 0\)

- **When there are no items**, the algorithm picks none.
- This is trivially optimal, as there is no way to gain any positive value from zero items.

Thus, **GreedyFKP** is correct for \(n = 0\).

---

## Inductive Hypothesis (IH): \(n = k\)

Assume that for **any** set of \(k\) items, **GreedyFKP** yields an optimal solution. Formally:

> For every problem instance of size \(k\), the solution chosen by **GreedyFKP** has the maximum possible total value among all feasible solutions.

---

## Inductive Step: \(n = k+1\)

We must show that **GreedyFKP** is optimal for any set of **\(k+1\)** items.

1. **Let** \(A = \{p_1, p_2, \dots, p_t\}\) be the set (or multiset) of items chosen by **GreedyFKP** for the \(k+1\) items.  
   - By design, \(p_1\) is the item with the **highest value/weight ratio** (or whichever greedy criterion applies).

2. **Let** \(O = \{q_1, q_2, \dots, q_r\}\) be **any optimal solution** for these \(k+1\) items (we do not yet assume \(p_1\in O\)).

---

### Step 1: Show There Exists an Optimal Solution Containing \(p_1\)

- **Case A**: If \(p_1 \in O\), then we are done; \(O\) already contains the optimal first choice.

- **Case B**: Suppose \(p_1 \notin O\). We argue by the **exchange method**:

  1. Since \(p_1\) was chosen first by **GreedyFKP**, its ratio \(\frac{p_1.\text{value}}{p_1.\text{mass}}\) is **at least as high** as that of any other item.
  
  2. Because \(O\) does not include \(p_1\), there must be some item \(q_i \in O\) whose ratio is **strictly lower** than \(p_1\)’s ratio.
  
  3. In the fractional knapsack setting, we can **replace** a fraction (or all) of \(q_i\) with \(p_1\). In doing so, we free up just enough capacity to include \(p_1\) (or the required fraction of \(p_1\)).
  
  4. **Value Comparison**: Since \(\text{ratio}(p_1) > \text{ratio}(q_i)\), swapping out part of \(q_i\) for \(p_1\) increases the total value. This results in a new solution \(O^*\) with a total value **greater** than or equal to that of \(O\), contradicting the optimality of \(O\) if \(O\) were better.
  
Thus, we can construct an optimal solution \(O^*\) that **does** include \(p_1\).

---

### Step 2: Show That \(A\) (GreedyFKP’s Solution) Is Optimal

1. Both \(A\) and the modified optimal solution \(O^*\) contain \(p_1\).

2. After choosing \(p_1\), the remaining problem is a **\(k\)-item** instance (or a knapsack of reduced capacity).

3. By the **Inductive Hypothesis**, **GreedyFKP** is optimal for any \(k\)-item instance.  
   - Therefore, the way \(A\) selects the remaining items (after \(p_1\)) is optimal.
   - \(O^*\) must also be optimal for that subproblem; hence, it cannot achieve a better result than \(A\) on the remaining \(k\) items.

4. Consequently, the total value of \(A\) matches that of \(O^*\). Since \(O^*\) is optimal, \(A\) must also be optimal.

---

## Conclusion

- The **base case** \((n=0)\) holds.
- Assuming optimality for \(k\) items (IH), we have shown that the algorithm remains optimal for \(k+1\) items.

By the principle of **mathematical induction**, **GreedyFKP** finds an **optimal** solution for all \(n\).

**Q.E.D.**
