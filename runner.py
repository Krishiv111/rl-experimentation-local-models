"""The grader. Reward = 1 if a task's tests pass, 0 if not."""

import tasks


def check(name, fn, cases):
    passed = True
    for args, expected in cases:
        try:
            got = fn(*args)
        except Exception as e:
            print(f"  {name}: ERROR on {args} -> {e}")
            passed = False
            continue
        if got != expected:
            print(f"  {name}: FAIL on {args} -> got {got!r}, expected {expected!r}")
            passed = False
    print(f"{name}: {'PASS' if passed else 'FAIL'}")
    return passed


def main():
    results = {}

    results["is_palindrome"] = check(
        "is_palindrome", tasks.is_palindrome,
        [(("racecar",), True), (("abc",), False), (("a",), True), (("",), True)],
    )

    results["max_of_list"] = check(
        "max_of_list", tasks.max_of_list,
        [(([3, 1, 4, 1, 5],), 5), (([-2, -9, -1],), -1)],
    )

    results["factorial"] = check(
        "factorial", tasks.factorial,
        [((5,), 120), ((0,), 1), ((1,), 1)],
    )

    results["last_k_elements"] = check(
        "last_k_elements", tasks.last_k_elements,
        [(([1, 2, 3, 4, 5], 2), [4, 5]), (([1, 2, 3], 3), [1, 2, 3])],
    )

    results["count_unique"] = check(
        "count_unique", tasks.count_unique,
        [(([1, 2, 2, 3, 1],), 3), (([],), 0), (([7],), 1)],
    )

    total = len(results)
    passed = sum(results.values())
    print(f"\n{passed}/{total} tasks passing")


if __name__ == "__main__":
    main()
