"""Checks every algorithm against a textbook example with a known answer.

Run with: python3 -m unittest test_algorithms
"""

import importlib.util
import os
import unittest

ROOT = os.path.dirname(os.path.abspath(__file__))


def load(path):
    # folders like 1d_linear aren't valid package names, so load by file path
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], os.path.join(ROOT, path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GRAPH = {"A": [("B", 1), ("C", 4)], "B": [("C", 2), ("D", 5)], "C": [("D", 1)], "D": []}


class DynamicProgramming(unittest.TestCase):
    def test_fibonacci(self):
        m = load("dynamic_programming/1d_linear/fibonacci.py")
        self.assertEqual([m.fib_dp(n) for n in range(8)], [0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(m.fib_recursive(15), m.fib_dp(15))

    def test_house_robber(self):
        self.assertEqual(load("dynamic_programming/1d_linear/house_robber.py").robbery([2, 7, 9, 3, 1]), 12)

    def test_max_subarray(self):
        m = load("dynamic_programming/1d_linear/max_subarray_sum.py")
        self.assertEqual(m.max_Subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_coin_change(self):
        self.assertEqual(load("dynamic_programming/1d_quadratic/coin_change.py").coin_change([1, 2, 5], 11), 3)

    def test_rod_cutting(self):
        m = load("dynamic_programming/1d_quadratic/rod_cutting.py")
        self.assertEqual(m.CutRod([0, 1, 5, 8, 9, 10, 17, 17, 20], 8), (22, 2))  # CLRS price table

    def test_unbounded_knapsack(self):
        m = load("dynamic_programming/1d_quadratic/unbounded_knapsack.py")
        self.assertEqual(m.unbounded_knapsack(8, [1, 3, 4, 5], [10, 40, 50, 70], 4), 110)

    def test_word_break(self):
        m = load("dynamic_programming/1d_quadratic/word_break.py")
        self.assertTrue(m.word_break({"leet", "code"}, "leetcode"))
        self.assertFalse(m.word_break({"cats", "dog", "sand", "and", "cat"}, "catsandog"))

    def test_min_path_sum(self):
        self.assertEqual(load("dynamic_programming/2d/min_path_sum.py").minimum_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)

    def test_lcs(self):
        m = load("dynamic_programming/2d/longest_common_subsequence.py")
        self.assertEqual(m.longest_common_subsequence("ABCBDAB", "BDCABA"), 4)

    def test_subset_sum(self):
        m = load("dynamic_programming/2d/subset_sum.py")
        self.assertTrue(m.subset_sum([3, 34, 4, 12, 5, 2], 9))
        self.assertFalse(m.subset_sum([3, 34, 4, 12, 5, 2], 30))


class BranchAndBound(unittest.TestCase):
    def test_shortest_trail_heap(self):
        m = load("branch_and_bound/shortest_trail_heap.py")
        self.assertEqual(m.branch_and_bound_shortest_path(GRAPH, "A", "D"), (["A", "B", "C", "D"], 4))
        self.assertEqual(m.branch_and_bound_shortest_path({"A": [], "B": []}, "A", "B"), (None, float("inf")))

    def test_shortest_trail_list(self):
        m = load("branch_and_bound/shortest_trail_list.py")
        self.assertEqual(m.branch_and_bound_with_list(GRAPH, "A", "D"), (["A", "B", "C", "D"], 4))

    def test_job_assignment(self):
        m = load("branch_and_bound/job_assignment.py")
        _, cost = m.job_assignment_bnb([[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]])
        self.assertEqual(cost, 13)


class Greedy(unittest.TestCase):
    def test_road_trip_iterative(self):
        m = load("greedy/road_trip/road_trip_iterative.py")
        self.assertEqual(m.road_trip_iterative([0, 100, 200, 350, 400], 200), [2])
        self.assertIsNone(m.road_trip_iterative([0, 100, 400], 200))


if __name__ == "__main__":
    unittest.main()
