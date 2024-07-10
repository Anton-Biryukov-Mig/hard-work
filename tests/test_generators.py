from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

transaction1 = {
    "state": "EXECUTED",
    "operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}},
    "description": "Transaction 1",
}
transaction2 = {
    "state": "EXECUTED",
    "operationAmount": {"amount": "200", "currency": {"name": "USD", "code": "USD"}},
    "description": "Transaction 2",
}


@pytest.fixture()
def transactions() -> List[Dict[str, Any]]:
    return [transaction1, transaction2]


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        ([transaction1], "USD", [transaction1]),
        ([transaction2], "USD", [transaction2]),
        ([], "USD", []),
    ],
)
def test_filter_by_currency(transactions: List[Dict[str, Any]], currency: str, expected: List[Dict[str, Any]]) -> None:
    """Тест filter_by_currency"""
    filtered_transactions = list(filter_by_currency(transactions, currency))
    assert filtered_transactions == expected


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        (
            [
                {
                    "state": "EXECUTED",
                    "operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Transaction 1",
                }
            ],
            "USD",
            ["Transaction 1"],
        ),
        (
            [
                {
                    "state": "EXECUTED",
                    "operationAmount": {"amount": "200", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Transaction 2",
                }
            ],
            "USD",
            ["Transaction 2"],
        ),
        ([], "USD", []),
    ],
)
def test_transaction_descriptions(transactions: List[Dict[str, Any]], currency: str, expected: List[str]) -> None:
    """Тест transaction_descriptions"""
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
    ],
)
def test_card_number_generator(start: int, end: int, expected: List[str]) -> None:
    """Тест card_number_generator"""
    generated_numbers = list(card_number_generator(start, end))
    assert generated_numbers == expected
