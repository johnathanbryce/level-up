def pair_sum_indices(data: list[tuple[str, int]], threshold: int):
    return [name for name, score in data if score > threshold]


print(
    pair_sum_indices(
        [("Alice", 85), ("Bob", 62), ("Charlie", 91), ("Diana", 74)], threshold=75
    )
)

print(pair_sum_indices([("Eli", 50), ("Fran", 49)], threshold=50))

print(pair_sum_indices([("Gina", 100)], threshold=99))
