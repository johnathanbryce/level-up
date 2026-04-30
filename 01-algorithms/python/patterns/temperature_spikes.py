# Pattern: hash-map-complement
# Temperature Spike Days
#
# You're analyzing daily high-temperature data for a weather service.
# Given a list `temps` of daily high temperatures (in order, oldest first)
# and an integer `k`, return a list of indices for days where the
# temperature was EXACTLY `k` degrees higher than SOME earlier day in
# the list.
#
# A "spike day" is any day i where there exists some j < i such that
# temps[i] - temps[j] == k.
#
# Constraints:
#   - 1 <= len(temps) <= 10**5
#   - -100 <= temps[i] <= 150
#   - 1 <= k <= 200
#   - Each spike day appears in the output at most once, even if
#     multiple earlier days match.
#   - Return the indices in ascending order.
#
# Examples:
#
#   temps = [60, 55, 70, 65, 75], k = 10
#   -> [2, 3, 4]
#       day 2 (70) matches day 0 (60)
#       day 3 (65) matches day 1 (55)
#       day 4 (75) matches day 3 (65)
#
#   temps = [50, 50, 50, 50], k = 5
#   -> []   (no pair has a difference of exactly 5)
#
#   temps = [10, 20, 30], k = 10
#   -> [1, 2]
#       day 1 (20) matches day 0 (10)
#       day 2 (30) matches day 1 (20)
#
#   temps = [100], k = 5
#   -> []   (only one day; no earlier day to compare against)


def temperature_spikes(temps: list[int], k: int) -> list[int]:
    temps_map = {}
    temps_k_index_list = []

    for i, temp in enumerate(temps):
        complement_lower_temp = temp - k

        # Check if complement exists as a KEY in temps_map
        if complement_lower_temp in temps_map:
            print(complement_lower_temp)
            temps_k_index_list.append(i)
        temps_map[temp] = i

    return temps_k_index_list


# --- tests ---
print(temperature_spikes([60, 55, 70, 65, 75], 10))  # expect [2, 3, 4]
print(temperature_spikes([50, 50, 50, 50], 5))  # expect []
print(temperature_spikes([10, 20, 30], 10))  # expect [1, 2]
print(temperature_spikes([100], 5))  # expect []
