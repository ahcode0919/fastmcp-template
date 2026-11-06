import runpy
from unittest.mock import MagicMock

import pytest

from example import calculator


@pytest.fixture
def mock_run(monkeypatch):
    run = MagicMock()
    monkeypatch.setattr(calculator.mcp, "run", run)
    return run


def test_main_runs_server(mock_run):
    calculator.main()
    mock_run.assert_called_once_with()


def test_python_m_runs_server(mock_run):
    runpy.run_module("example", run_name="__main__")
    mock_run.assert_called_once_with()
