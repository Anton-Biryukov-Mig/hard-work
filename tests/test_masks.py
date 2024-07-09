from typing import List, Tuple

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_numbers() -> List[Tuple[str, str]]:
    return [
        ("Visa 1234 5678 9012 3456", "Visa 1234 56** **** 3456"),
        ("Maestro 9876 5432 1098 7654", "Maestro 9876 54** **** 7654"),
        ("123456789012345", "Неверный формат входных данных"),
    ]


def test_get_mask_card_number(card_numbers: List[Tuple[str, str]]) -> None:
    """Тест функции get_mask_card_number"""
    for input_val, expected_output in card_numbers:
        assert get_mask_card_number(input_val) == expected_output

    card_numbers = [
        ("Visa 1234 5678 9012 3456", "Visa 1234 56** **** 3456"),
        ("Maestro 9876 5432 1098 7654", "Maestro 9876 54** **** 7654"),
        ("123456789012345", "Неверный формат входных данных"),
    ]

    for input_val, expected_output in card_numbers:
        assert get_mask_card_number(input_val) == expected_output


@pytest.fixture
def account_numbers() -> List[Tuple[str, str]]:
    return [("1234567890", "Счет **7890"), ("9876543210", "Счет **3210"), ("12345", "Счет **2345")]


def test_get_mask_account(account_numbers: List[Tuple[str, str]]) -> None:
    """Тест функции get_mask_account"""
    for input_val, expected_output in account_numbers:
        assert get_mask_account(input_val) == expected_output

    account_numbers = [
        ("1234567890", "Счет **7890"),
        ("9876543210", "Счет **3210"),
        ("12345", "Счет **2345"),
    ]

    for input_val, expected_output in account_numbers:
        assert get_mask_account(input_val) == expected_output

