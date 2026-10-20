"""Tiny project used to exercise the harness trusted CI."""


def mean(values):
    """Return the arithmetic mean of a non-empty list of numbers."""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def median(values):
    """Return the median of a non-empty list of numbers."""
    if not values:
        raise ValueError("values must not be empty")
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def mode(values):
    """Return the most common value (the smallest one on ties)."""
    if not values:
        raise ValueError("values must not be empty")
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    best = max(counts.values())
    return min(v for v, c in counts.items() if c == best)
