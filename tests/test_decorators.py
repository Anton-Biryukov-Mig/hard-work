from typing import Any, Optional

import pytest

from src.decorators import log


@log(filename="src\\mylog.txt")  # Using double backslashes
def my_function(x: int, y: int) -> int:
    """Add two integers and return the result.

    Args:
        x (int): The first integer.
        y (int): The second integer.

    Returns:
        int: The sum of x and y.
    """
    return x + y


@pytest.mark.parametrize("filename", [None, "src\\mylog.txt"])  # Using double backslashes
def test_log(capsys: Any, filename: Optional[str]) -> None:
    """Test the log decorator.

    Args:
        capsys (Any): The pytest fixture for capturing stdout/stderr.
        filename (Optional[str]): The filename for logging.
    """

    @log(filename)
    def test_func() -> None:
        """Test function.

        Returns:
            None
        """
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
