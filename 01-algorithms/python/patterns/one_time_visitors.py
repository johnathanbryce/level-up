# A server log records the IP address of every request.
# Return only the IPs that appear exactly once, in the order they first appeared.
#
# one_time_visitors(["1.1.1.1", "2.2.2.2", "1.1.1.1", "3.3.3.3"])  → ["2.2.2.2", "3.3.3.3"]
# one_time_visitors(["9.9.9.9"])                                     → ["9.9.9.9"]
# one_time_visitors(["1.1.1.1", "1.1.1.1", "1.1.1.1"])              → []
# one_time_visitors(["a", "b", "c", "b", "d"])                      → ["a", "c", "d"]
#
# Constraints: list may be empty (return []), all entries are non-empty strings


# Pattern: frequency counting (count-then-inspect)
def one_time_visitors(log) -> list:
    from collections import Counter

    counts = Counter(log)                          # pass 1: count everything — O(n)
    return [ip for ip in log if counts[ip] == 1]  # pass 2: filter — O(n)


# Tests
print(
    one_time_visitors(["1.1.1.1", "2.2.2.2", "1.1.1.1", "3.3.3.3"])
)  # ["2.2.2.2", "3.3.3.3"]
print(one_time_visitors(["9.9.9.9"]))  # ["9.9.9.9"]
print(one_time_visitors(["1.1.1.1", "1.1.1.1", "1.1.1.1"]))  # []
print(one_time_visitors(["a", "b", "c", "b", "d"]))  # ["a", "c", "d"]
