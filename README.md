# CISC 365 algorithms

Algorithms from CISC 365 (Algorithms I) at Queen's, winter 2025. The two divide-and-conquer files are the course's practice solutions, not mine. The `notes.pdf` files are my handwritten notes and the `proof.md` files are the correctness proofs I wrote for the greedy algorithms.

```
greedy/                 activity selection, coin change, fractional knapsack, road trip (recursive and iterative)
divide_and_conquer/     majority element, find the single letter (Prof. Ting Hu's practice solutions, kept for reference)
dynamic_programming/
  1d_linear/            Fibonacci (DP vs naive recursion), house robber, max subarray sum
  1d_quadratic/         coin change, rod cutting, unbounded knapsack, word break
  2d/                   longest common subsequence, min path sum, subset sum, pacman with ghosts
branch_and_bound/       shortest path (heap and list frontiers), job assignment
```

All of the DP solutions are bottom-up tables. The branch and bound shortest path keeps a global upper bound from the best complete path so far and prunes any partial path that already costs more; the two versions differ only in whether the frontier is a heap or a plain list.

Each algorithm is checked against a standard example with a known answer:

```bash
python3 -m unittest test_algorithms
```
