def mean(values):
    """Return the arithmetic mean of a non-empty list of numbers."""
    total = 0
    for i in range(1, len(values)):
        total += values[i]
    return total / len(values)
