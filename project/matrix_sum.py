"""
Given an m x n matrix of rooms and each room having a random cost to enter the room:

          m
     --- --- ---
    | 1 | 3 | 2 |
     --- --- ---
  n | 1 | 5 | 7 |
     --- --- ---
    | 3 | 4 | 2 |
     --- --- ---

Generate a set of unique costs to travel from the top-left-most room to the bottom-right-most room.
Note that you can only travel in 2-directions: right or down from any given room.

The function will be passed in A as a list of lists:

Examples:

    A: [[0, 1], [1, 2]]
    r: set([3])

    A: [[1, 2, 3], [4, 5, 6]]
    r: set([12, 14, 16])
"""
import project.config as config


class Solution():
    def maze_sum_set(self, A):
        if not A: return set()
        if not A[0]: return set()

        m = len(A[0])
        n = len(A)
        paths = [{"sum":A[0][0], "m": 0, "n": 0}]
        if config.debug: print("m: %s n: %s" % (m, n))
        for pos in paths:
            # Can I go right?
            if pos["m"] < m-1:
                cm = pos["m"] + 1
                cn = pos["n"]
                new_sum = pos["sum"] + A[cn][cm]
                paths.append({"sum":new_sum, "m": cm, "n": cn})
            # Can I go down?
            if pos["n"] < n-1:
                cm = pos["m"]
                cn = pos["n"] + 1
                new_sum = pos["sum"] + A[cn][cm]
                paths.append({"sum":new_sum, "m": cm, "n": cn})

        if config.debug: print(paths)
        return {pos["sum"] for pos in paths if pos["m"] == (m-1) and pos["n"] == (n-1)}

