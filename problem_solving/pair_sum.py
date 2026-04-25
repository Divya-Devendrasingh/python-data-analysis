def find_pairs(arr, target):
    seen = set()
    pairs = set()

    for n in arr:
        diff = target - n

        if diff in seen:
            pairs.add((min(n, diff), max(n, diff)))
        else:
            seen.add(n)

    return list(pairs)


print(find_pairs([1, 2, 3, 4, 5], 6))
