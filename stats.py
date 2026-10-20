"""Tiny project used to exercise the harness trusted CI."""


def mean(values):
    """Return the arithmetic mean of a non-empty list of numbers."""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values[1:]) / len(values)


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
