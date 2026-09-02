import math

import pytest

from extended_intro_hw3 import (
    NR,
    diff_param,
    equal,
    find_root1,
    find_root2,
    find_root_range,
    generate_sorted_blocks,
    inverse,
    merge,
    merge_sorted_blocks,
    selection_sort,
    sort_by_block_merge,
    sort_triplets1,
    sort_triplets2,
    source,
)


def test_linear_root_search() -> None:
    assert find_root1(lambda value: value - 8) == 8
    assert find_root1(lambda value: value + 1) is None


def test_range_root_search() -> None:
    assert find_root_range(lambda value: value - 4, 3, 10) == 4
    assert find_root_range(lambda value: 4 - value, 1.2, 8.9) == 4
    assert find_root_range(lambda value: value - 20, 6, 19) is None


def test_exponential_root_search() -> None:
    assert find_root2(lambda value: value - 5) == 5
    assert abs(find_root2(lambda value: value**2 - 4)) == 2
    assert find_root2(lambda value: 2 * value + 1) is None


def test_selection_sort_is_in_place() -> None:
    values = [4, 1, 3, 1]

    assert selection_sort(values) is None
    assert values == [1, 1, 3, 4]


def test_generate_sorted_blocks_does_not_mutate_input() -> None:
    values = [610, 906, 308, 759, 15, 389, 892, 939, 685, 565]

    assert generate_sorted_blocks(values, 3) == [
        [308, 610, 906],
        [15, 389, 759],
        [685, 892, 939],
        [565],
    ]
    assert values[0] == 610


def test_block_generation_rejects_non_positive_size() -> None:
    with pytest.raises(ValueError):
        generate_sorted_blocks([1, 2], 0)


def test_merge_and_merge_sorted_blocks() -> None:
    assert merge([1, 4, 7], [2, 2, 8]) == [1, 2, 2, 4, 7, 8]
    assert merge_sorted_blocks([[19, 156, 322], [11, 188, 921], [222, 543]]) == [
        11,
        19,
        156,
        188,
        222,
        322,
        543,
        921,
    ]
    assert merge_sorted_blocks([]) == []


@pytest.mark.parametrize("block_size", [1, 2, 3, 10, 20])
def test_block_merge_matches_reference_order(block_size: int) -> None:
    values = [610, 906, 308, 759, 15, 389, 892, 939, 685, 565]
    assert sort_by_block_merge(values, block_size) == sorted(values)


@pytest.mark.parametrize("function", [sort_triplets1, sort_triplets2])
def test_triplet_sorting_preserves_duplicates_and_input(function) -> None:
    values = [(4, 2, 1), (1, 4, 3), (4, 2, 1), (0, 0, 2)]

    assert function(values, 5) == [(0, 0, 2), (1, 4, 3), (4, 2, 1), (4, 2, 1)]
    assert values[0] == (4, 2, 1)


@pytest.mark.parametrize("function", [sort_triplets1, sort_triplets2])
def test_triplet_sorting_validates_coordinate_limit(function) -> None:
    with pytest.raises(ValueError):
        function([(0, 5, 0)], 5)


def test_finite_difference_approximates_derivative() -> None:
    derivative = diff_param(lambda value: value**2, 1e-6)
    assert derivative(3) == pytest.approx(6, abs=1e-5)


def test_newton_raphson_converges_and_handles_zero_derivative() -> None:
    root = NR(lambda value: value**2 - 9, lambda value: 2 * value, x0=2)
    assert root == pytest.approx(3)
    assert NR(lambda value: value**2 + 1, lambda _value: 0, x0=1) is None


def test_equal_source_and_inverse() -> None:
    assert equal(lambda value: 4 * value + 1, lambda value: -value + 6) == pytest.approx(1)
    assert source(lambda value: value + 3, 5) == pytest.approx(2)
    assert inverse(lambda value: value**3)(-27) == pytest.approx(-3)


def test_inverse_reports_non_convergence() -> None:
    with pytest.raises(ValueError):
        inverse(lambda _value: 1)(2)


def test_numerical_results_are_finite() -> None:
    result = source(math.exp, math.e)
    assert result is not None and math.isfinite(result)
