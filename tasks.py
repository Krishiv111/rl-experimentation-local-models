"""5 tasks, each one small function with exactly one planted bug.

Each bug is a realistic mistake pattern, not a random break:
  1. off-by-one in a loop boundary
  2. wrong comparison operator
  3. missing/incorrect base case
  4. inclusive/exclusive boundary bug on a slice
  5. variable not reset between iterations
"""


def is_palindrome(s: str) -> bool:
    # bug: off-by-one — stops one char before the midpoint, misses the center check
    n = len(s)
    for i in range(n // 2 - 1):
        if s[i] != s[n - 1 - i]:
            return False
    return True


def max_of_list(nums: list[int]) -> int:
    # bug: wrong comparison operator — uses >= so it still works, flip to find the real bug class
    # (this one is intentionally correct, as a control task — not every task should be broken)
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
    return m


def factorial(n: int) -> int:
    # bug: missing base case — recurses forever / hits recursion limit at n == 0
    if n == 1:
        return 1
    return n * factorial(n - 1)


def last_k_elements(nums: list[int], k: int) -> list[int]:
    # bug: off-by-one slice boundary — drops the final element
    return nums[len(nums) - k - 1:]


def count_unique(nums: list[int]) -> int:
    # bug: `seen` never resets between elements it shouldn't reset on,
    # but here the real bug is initializing it inside the loop, so it never accumulates
    count = 0
    for n in nums:
        seen = set()
        if n not in seen:
            seen.add(n)
            count += 1
    return count
