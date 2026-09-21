"""Command-line interface for the Homework 3 sorting algorithms."""

from __future__ import annotations

import argparse

from extended_intro_hw3 import sort_by_block_merge, sort_triplets1, sort_triplets2


def triplet(value: str) -> tuple[int, int, int]:
    try:
        coordinates = tuple(int(item) for item in value.split(","))
    except ValueError as error:
        raise argparse.ArgumentTypeError("triplets must use integer a,b,c syntax") from error
    if len(coordinates) != 3:
        raise argparse.ArgumentTypeError("triplets must contain exactly three coordinates")
    return coordinates


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    block_parser = subparsers.add_parser("block-sort")
    block_parser.add_argument("block_size", type=int)
    block_parser.add_argument("values", type=int, nargs="+")

    for command in ("triplet-enumeration-sort", "triplet-selection-sort"):
        triplet_parser = subparsers.add_parser(command)
        triplet_parser.add_argument("limit", type=int)
        triplet_parser.add_argument("values", type=triplet, nargs="+")
    return parser


def cli() -> None:
    arguments = build_parser().parse_args()
    try:
        if arguments.command == "block-sort":
            result = sort_by_block_merge(arguments.values, arguments.block_size)
        elif arguments.command == "triplet-enumeration-sort":
            result = sort_triplets1(arguments.values, arguments.limit)
        else:
            result = sort_triplets2(arguments.values, arguments.limit)
        print(result)
    except ValueError as error:
        raise SystemExit(f"error: {error}") from error


if __name__ == "__main__":
    cli()
