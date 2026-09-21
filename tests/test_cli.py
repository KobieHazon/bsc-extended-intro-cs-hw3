from extended_intro_hw3_cli import cli


def test_block_sort_cli(monkeypatch, capsys) -> None:
    monkeypatch.setattr("sys.argv", ["extended-intro-hw3", "block-sort", "3", "5", "1", "4", "2"])

    cli()

    assert capsys.readouterr().out == "[1, 2, 4, 5]\n"


def test_triplet_sort_cli(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        "sys.argv",
        ["extended-intro-hw3", "triplet-selection-sort", "5", "4,2,1", "1,4,3"],
    )

    cli()

    assert capsys.readouterr().out == "[(1, 4, 3), (4, 2, 1)]\n"
