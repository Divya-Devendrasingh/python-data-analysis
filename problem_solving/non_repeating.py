def first_nonrep(numbers):
    count = {}

    for n in numbers:
        count[n] = count.get(n, 0) + 1

    for n in numbers:
        if count[n] == 1:
            return n


print(first_nonrep([4, 5, 6, 5, 4, 3, 2]))
