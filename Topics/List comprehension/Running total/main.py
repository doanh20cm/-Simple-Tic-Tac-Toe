numbers = [int(_) for _ in input()]
print([sum(numbers[:_ + 1]) for _ in range(len(numbers))])