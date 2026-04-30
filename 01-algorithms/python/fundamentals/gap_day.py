def gap_day_exists(counts: list[int], k: int) -> bool:

    seen_counts = set()
    for count in counts:
        earlier_day = count + k

        if earlier_day in seen_counts:
            return True

        seen_counts.add(count)

    return False


# Tests
print(gap_day_exists([14, 10, 18, 12, 16], 4))  # True  — 14 and 10: 14-10=4
print(gap_day_exists([5, 8, 11, 3], 7))  # False — no pair with diff 7
print(gap_day_exists([20, 15, 20, 14], 6))  # True  — 20 and 14: 20-14=6
print(gap_day_exists([7, 7, 7], 0))  # True  — same value, diff=0
