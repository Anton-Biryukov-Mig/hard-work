import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_data, mask_account_card


# Фикстура для предоставления тестовых данных для функции get_mask_card_number
@pytest.fixture
def card_numbers():
    return [
        ("Visa 1234 5678 9012 3456", "Visa 1234 ** **** 3456"),
        ("Maestro 9876 5432 1098 7654", "Maestro 9876 ** **** 7654"),
        ("123456789012345", "Неверный формат входных данных"),
    ]


# Тесты для функции get_mask_card_number
def test_get_mask_card_number(card_numbers):
    for input_val, expected_output in card_numbers:
        assert get_mask_card_number(input_val) == expected_output


# Фикстура для предоставления тестовых данных для функции get_mask_account
@pytest.fixture
def account_numbers():
    return [("Счет 1234567890", "Счет **7890"), ("Счет 9876543210", "Счет **3210"), ("12345", "Счет **2345")]


# Тесты для функции get_mask_account
def test_get_mask_account(account_numbers):
    for input_val, expected_output in account_numbers:
        assert get_mask_account(input_val) == expected_output


# Тест для функции mask_account_card
def test_mask_account_card():
    assert mask_account_card("Visa Platinum 1234 5678 9012 3456") == "Visa 1234 ** **** 3456"
    assert mask_account_card("Maestro 9876 5432 1098 7654") == "Maestro 9876 ** **** 7654"
    assert mask_account_card("Счет 1234567890") == "Счет **7890"
    assert mask_account_card("Invalid Input") is None


# Тест для функции get_data
def test_get_data():
    assert get_data("2023-12-31T15:30:00.000Z") == "31.12.2023"
    assert get_data("2022-08-15T10:45:00.000Z") == "15.08.2022"
    assert get_data("Invalid Input") is None


# Фикстура для предоставления тестовых данных для функции filter_by_state и sort_by_date
@pytest.fixture
def sample_data():
    return [
        {"state": "EXECUTED", "date": "2023-12-31T15:30:00.000Z"},
        {"state": "PENDING", "date": "2022-08-15T10:45:00.000Z"},
        {"state": "EXECUTED", "date": "2024-05-20T18:00:00.000Z"},
    ]


# Тест для функции filter_by_state
def test_filter_by_state(sample_data):
    assert filter_by_state(sample_data, "EXECUTED") == [
        {"state": "EXECUTED", "date": "2023-12-31T15:30:00.000Z"},
        {"state": "EXECUTED", "date": "2024-05-20T18:00:00.000Z"},
    ]
    assert filter_by_state(sample_data, "PENDING") == [{"state": "PENDING", "date": "2022-08-15T10:45:00.000Z"}]


# Тест для функции sort_by_date
def test_sort_by_date(sample_data):
    assert sort_by_date(sample_data) == [
        {"state": "EXECUTED", "date": "2024-05-20T18:00:00.000Z"},
        {"state": "EXECUTED", "date": "2023-12-31T15:30:00.000Z"},
        {"state": "PENDING", "date": "2022-08-15T10:45:00.000Z"},
    ]
    assert sort_by_date(sample_data, reverse=False) == [
        {"state": "PENDING", "date": "2022-08-15T10:45:00.000Z"},
        {"state": "EXECUTED", "date": "2023-12-31T15:30:00.000Z"},
        {"state": "EXECUTED", "date": "2024-05-20T18:00:00.000Z"},
    ]
