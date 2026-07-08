"""
Task 3 - Bottom-up dynamic programming for the recurrence

    S(k) = 2                                    if 0 <= k <= 1
    S(k) = 3 * sum_{i=1}^{k-1} S(i) * S(i-1)     if k > 1

A running accumulator carries the partial sum forward between
iterations so each new S(k) is computed in O(1) amortized work,
giving O(k) total time instead of the O(k^2) a naive re-summation
would cost.
"""

from typing import List


def compute_S(k_max: int) -> List[int]:
    S: List[int] = [0] * (k_max + 1)
    
    S[0]: int = 2
    if k_max == 0:
        return S

    S[1]: int = 2
    if k_max == 1:
        return S

    running_sum: int = S[1] * S[0]  

    for k in range(2, k_max + 1):
        S[k]: int = 3 * running_sum
        running_sum: int = running_sum + S[k] * S[k - 1]  

    return S


if __name__ == "__main__":
    table: List[int] = compute_S(6)
    for k, value in enumerate(table):
        k: int
        value: int
        print(f"S({k}) = {value}")
