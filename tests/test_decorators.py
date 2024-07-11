from typing import Any, Optional

import pytest

from src.decorators import log


@log(filename="src\\mylog.txt")  # Using double backslashes
def my_function(x: int, y: int) -> int:
    """Сложите два целых числа и верните результат"""
    return x + y


@pytest.mark.parametrize("filename", [None, "src\\mylog.txt"])  # Using double backslashes
def test_log(capsys: Any, filename: Optional[str]) -> None:
    """Тест log"""

    @log(filename)
    def test_func() -> None:
        """Тест func"""
        my_function(1, 2)

    test_func()

    captured = capsys.readouterr()

    if filename:
        try:
            with open(filename, "r") as file:
                log_content = file.read()
                assert "test_func ok" in log_content
        except FileNotFoundError:
            pytest.fail(f"File '{filename}' not found.")
    else:
        assert "test_func ok" in captured.out
