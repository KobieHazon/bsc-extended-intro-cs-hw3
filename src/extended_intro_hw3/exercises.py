"""Maintained implementations of the Homework 3 programming questions."""

from __future__ import annotations

import math
from collections.abc import Callable, Sequence
from typing import TypeVar

T = TypeVar("T")
Triplet = tuple[int, int, int]
RealFunction = Callable[[float], float]
MAX_ROOT_SEARCH = 1_000_000


def find_root1(function: Callable[[int], float]) -> int | None:
    """Find a positive integer root by linear search under the assignment assumptions."""
    first = function(1)
    if first == 0:
        return 1
    second = function(2)
    if (second > first > 0) or (second < first < 0):
        return None
    for candidate in range(2, MAX_ROOT_SEARCH + 1):
        if function(candidate) == 0:
            return candidate
    return None


def find_root_range(function: Callable[[int], float], start: float, end: float) -> int | None:
    """Find an integer root of a monotone function in a closed real interval."""
    left = math.ceil(start)
    right = math.floor(end)
    if left > right:
        return None

    left_value = function(left)
    right_value = function(right)
    if left_value == 0:
        return left
    if right_value == 0:
        return right
    if left_value * right_value > 0:
        return None

    increasing = left_value < right_value
    while left <= right:
        middle = (left + right) // 2
        value = function(middle)
        if value == 0:
            return middle
        if (increasing and value < 0) or (not increasing and value > 0):
            left = middle + 1
        else:
            right = middle - 1
    return None


def find_root2(function: Callable[[int], float]) -> int | None:
    """Find an integer root by exponentially expanding around zero."""
    if function(0) == 0:
        return 0
    previous_radius = 0
    for exponent in range(21):
        radius = 1 << exponent
        for start, end in (
            (previous_radius, radius),
            (-radius, -previous_radius),
        ):
            result = find_root_range(function, start, end)
            if result is not None:
                return result
        previous_radius = radius
    return None


def swap(values: list[T], first: int, second: int) -> None:
    """Swap two list entries in place."""
    values[first], values[second] = values[second], values[first]


def selection_sort(values: list[T]) -> None:
    """Sort a list in place using selection sort."""
    for index in range(len(values)):
        minimum = min(range(index, len(values)), key=values.__getitem__)
        swap(values, index, minimum)


def generate_sorted_blocks(values: Sequence[T], block_size: int) -> list[list[T]]:
    """Copy a sequence into independently selection-sorted blocks."""
    if block_size < 1:
        raise ValueError("block_size must be positive")
    blocks: list[list[T]] = []
    for start in range(0, len(values), block_size):
        block = list(values[start : start + block_size])
        selection_sort(block)
        blocks.append(block)
    return blocks


def merge(first: Sequence[T], second: Sequence[T]) -> list[T]:
    """Merge two sorted sequences."""
    merged: list[T] = []
    first_index = second_index = 0
    while first_index < len(first) and second_index < len(second):
        if first[first_index] <= second[second_index]:
            merged.append(first[first_index])
            first_index += 1
        else:
            merged.append(second[second_index])
            second_index += 1
    merged.extend(first[first_index:])
    merged.extend(second[second_index:])
    return merged


def merge_sorted_blocks(blocks: Sequence[Sequence[T]]) -> list[T]:
    """Repeatedly merge adjacent sorted blocks into one sorted list."""
    current = [list(block) for block in blocks]
    if not current:
        return []
    while len(current) > 1:
        next_level: list[list[T]] = []
        for index in range(0, len(current), 2):
            if index + 1 == len(current):
                next_level.append(current[index])
            else:
                next_level.append(merge(current[index], current[index + 1]))
        current = next_level
    return current[0]


def sort_by_block_merge(values: Sequence[T], block_size: int) -> list[T]:
    """Sort by selection-sorting fixed blocks and merge them pairwise."""
    return merge_sorted_blocks(generate_sorted_blocks(values, block_size))


def sort_triplets1(values: Sequence[Triplet], limit: int) -> list[Triplet]:
    """Sort bounded triplets by enumerating the complete coordinate space."""
    counts = _triplet_counts(values, limit)
    result: list[Triplet] = []
    for first in range(limit):
        for second in range(limit):
            for third in range(limit):
                triplet = (first, second, third)
                result.extend([triplet] * counts.get(triplet, 0))
    return result


def sort_triplets2(values: Sequence[Triplet], limit: int) -> list[Triplet]:
    """Sort bounded triplets with a non-mutating selection sort."""
    _triplet_counts(values, limit)
    result = list(values)
    selection_sort(result)
    return result


def diff_param(function: RealFunction, step: float = 0.001) -> RealFunction:
    """Return a forward finite-difference derivative approximation."""
    if step == 0:
        raise ValueError("step must be non-zero")
    return lambda value: (function(value + step) - function(value)) / step


def NR(
    function: RealFunction,
    derivative: RealFunction,
    epsilon: float = 10**-8,
    iterations: int = 100,
    x0: float | None = None,
) -> float | None:
    """Approximate a root with bounded Newton-Raphson iteration."""
    if epsilon <= 0 or iterations < 1:
        raise ValueError("epsilon and iterations must be positive")
    value = 1.0 if x0 is None else float(x0)
    try:
        for _ in range(iterations):
            function_value = function(value)
            if abs(function_value) < epsilon:
                return value
            slope = derivative(value)
            if abs(slope) < epsilon:
                return None
            value -= function_value / slope
            if not math.isfinite(value):
                return None
    except (ArithmeticError, OverflowError, ValueError):
        return None
    return None


def equal(first: RealFunction, second: RealFunction) -> float | None:
    """Approximate an intersection between two functions."""

    def difference(value: float) -> float:
        return first(value) - second(value)

    return NR(difference, diff_param(difference))


def source(function: RealFunction, target: float) -> float | None:
    """Approximate a source value that maps to ``target``."""

    def difference(value: float) -> float:
        return function(value) - target

    return NR(difference, diff_param(difference))


def inverse(function: RealFunction) -> RealFunction:
    """Return a numerical inverse function."""

    def inverse_function(target: float) -> float:
        result = source(function, target)
        if result is None:
            raise ValueError("the inverse approximation did not converge")
        return result

    return inverse_function


def _triplet_counts(values: Sequence[Triplet], limit: int) -> dict[Triplet, int]:
    if limit < 1:
        raise ValueError("limit must be positive")
    counts: dict[Triplet, int] = {}
    for triplet in values:
        if len(triplet) != 3 or any(
            coordinate < 0 or coordinate >= limit for coordinate in triplet
        ):
            raise ValueError("every coordinate must be in range(limit)")
        counts[triplet] = counts.get(triplet, 0) + 1
    return counts
