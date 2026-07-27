"""
S(k) = 2 if 0 <= k <= 1
S(k) = 3 * sum_{i=1}^{k-1} S(i) * S(i-1)     if k > 1
"""


def compute_S(k_max: int) -> list[int]:
    if k_max < 0:
        raise ValueError("k_max must be non-negative")

    S: list[int] = [0] * (k_max + 1)

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
    table: list[int] = compute_S(6)
    for k, value in enumerate(table):
        k: int
        value: int
        print(f"S({k}) = {value}")
