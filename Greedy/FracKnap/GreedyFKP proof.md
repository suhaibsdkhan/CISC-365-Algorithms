Below is a **refined** and **clearer** write-up of your two-step inductive proof. It maintains the structure you provided but clarifies the **exchange argument** and logical details.

---

## **Proof by Induction**

We want to prove that the **GreedyFKP** algorithm finds an **optimal** solution (i.e., a solution with maximum total value) for the fractional knapsack problem.

### **Base Case: \(n = 0\)**

- If there are **no items**, the algorithm picks none.
- This is trivially optimal, as there is no way to gain any positive value from zero items.
  
Hence, **GreedyFKP** is correct for \(n = 0\).

---

### **Inductive Hypothesis (IH): \(n = k\)**

Assume that for **any** set of \(k\) items, **GreedyFKP** yields an optimal solution. Formally:

> For every problem instance of size \(k\), the solution chosen by **GreedyFKP** has the maximum possible total value among all feasible solutions.

---

### **Inductive Step: \(n = k+1\)**

We must show that **GreedyFKP** is optimal for any set of **\(k+1\)** items.

1. **Let \(A = \{p_1, p_2, \dots, p_t\}\)** be the set (or multiset) of items chosen by **GreedyFKP** for the \(k+1\) items.  
   - By design, \(p_1\) is the item with the **highest value/weight ratio** (or whichever greedy criterion applies).  
2. **Let \(O = \{q_1, q_2, \dots, q_r\}\)** be **any optimal solution** for these \(k+1\) items (we do not yet assume \(p_1\in O\)).

We split the argument into two parts:

---

#### **Step 1: Show there is an optimal solution containing \(p_1\)**

- **Case A**: \(p_1 \in O\) already.  
  Then we are done: \(O\) itself is an optimal solution that includes \(p_1\).

- **Case B**: \(p_1 \notin O\).  
  We claim this leads to a **contradiction** if \(O\) is truly optimal. The usual **exchange argument** is:

  1. Since \(p_1\) was chosen first by **GreedyFKP**, its ratio \(\frac{p_1.\text{value}}{p_1.\text{mass}}\) is **at least as large** as that of **any** other item in the set.  
  2. Because \(O\) does *not* contain \(p_1\), there must be some item \(q_i \in O\) whose ratio is **strictly lower** than \(p_1\)’s ratio.  
  3. **Replace** part (or all) of \(q_i\) in \(O\) with \(p_1\). In the fractional knapsack setting, you can remove a fraction of \(q_i\)’s mass to free up exactly enough capacity for \(p_1\) (or the fraction of \(p_1\) you need).  
  4. **Value Comparison**: Because \(\text{ratio}(p_1) > \text{ratio}(q_i)\), swapping out some portion of \(q_i\) for \(p_1\) *increases* the total value, making a strictly better solution than \(O\). This contradicts the assumption that \(O\) was optimal.

Hence, we can construct a new solution \(O^*\) (starting from \(O\)) that **does** include \(p_1\) and has value at least as large as \(O\). Therefore, there exists an optimal solution that contains \(p_1\).

---

#### **Step 2: Show that \(A\) (GreedyFKP’s solution) is optimal**

Now that we know there is **some** optimal solution \(O^*\) which includes \(p_1\), we compare \(A\) and \(O^*\):

1. **Both** \(A\) and \(O^*\) include \(p_1\).  
2. After picking \(p_1\), the remaining problem is effectively a **\(k\)-item** problem (or a knapsack of reduced capacity).  
3. By the **Inductive Hypothesis**, **GreedyFKP** is optimal for any \(k\)-item instance.  
   - Therefore, the way \(A\) picks items (after \(p_1\)) is **optimal** for the remaining capacity.  
   - \(O^*\) must also be an optimal choice for that same subproblem, so it cannot do any better than \(A\) on those remaining \(k\) items.  
4. Consequently, \(A\) and \(O^*\) have the **same total value**. Since \(O^*\) is optimal, \(A\) must be optimal as well.

---

## **Conclusion**

- We verified the **base case** \((n=0)\).  
- We showed that if **GreedyFKP** is optimal for all \(k\)-item instances, it remains optimal for \((k+1)\)-item instances.  

By the principle of **mathematical induction**, **GreedyFKP** finds an **optimal** solution for **all** \(n\). 

**Q.E.D.**