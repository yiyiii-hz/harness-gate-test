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


def variance(values):
    """Return the population variance (divided by n) of a non-empty list of numbers."""
    if not values:
        raise ValueError("values must not be empty")
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)


def stdev(values):
    """Return the population standard deviation (square root of variance) of a non-empty list of numbers."""
    if not values:
        raise ValueError("values must not be empty")
    return variance(values) ** 0.5


def range_(values):
    """Return the range (maximum minus minimum) of a non-empty list of numbers."""
    if not values:
        raise ValueError("values must not be empty")
    return max(values) - min(values)
