from __future__ import annotations

import threading
from pathlib import Path

import extended_intro_hw3

REPOSITORY_ROOT = Path(__file__).parents[1]


def test_maintained_implementation_passes_supplied_tester(monkeypatch, capsys) -> None:
    monkeypatch.setattr(threading.Thread, "isAlive", threading.Thread.is_alive, raising=False)
    namespace = {name: getattr(extended_intro_hw3, name) for name in extended_intro_hw3.__all__}
    tester = REPOSITORY_ROOT / "assignment/hw3_tester.py"

    exec(compile(tester.read_text(encoding="utf-8"), str(tester), "exec"), namespace)

    output = capsys.readouterr().out
    assert "Reduced grade:  0" in output
    assert "Error in" not in output
