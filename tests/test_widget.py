import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("Visa Platinum 1234 5678 9012 3456", "Visa Platinum 1234 56** **** 3456"),
        ("Maestro 9876543210987654", "Maestro 9876 54** **** 7654"),
        ("Счет 1234567890", "Счет **7890"),
        ("Счет 9876543210", "Счет **3210"),
        ("Счет 12345", "Счет **2345"),
        ("Invalid Input", None),
    ],
)
def test_mask_account_card(input_string: str, expected_output: str) -> None:
    """Тест функции mask_account_card"""
    if "Visa Platinum" in input_string or "Maestro" in input_string:
        assert mask_account_card(input_string) == expected_output
    elif "Счет" in input_string:
        assert mask_account_card(input_string) == expected_output
    else:
        assert mask_account_card(input_string) is None


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("2023-12-31T15:30:00.000", "31.12.2023"),
        ("2022-08-15T10:45:00.000", "15.08.2022"),
        ("2024-05-20T18:00:00.000", "20.05.2024"),
    ],
)
def test_get_data(input_string: str, expected_output: str) -> None:
    """Тест функции get_data"""
    assert get_data(input_string) == expected_output

