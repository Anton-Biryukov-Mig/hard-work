import unittest
from typing import Any, Dict
from unittest.mock import patch

from src.external_api import amount_transaction


@patch("src.external_api.requests.request")
def test_amount_transaction_rub(mock_request: Any) -> None:
    """Проверяем, что транзакция в рублях корректно обрабатывается"""
    mock_request.return_value.json.return_value = {"result": 31957.58}
    transaction: Dict[str, Any] = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
    }
    result: float = amount_transaction(transaction)
    assert result == 31957.58


@patch("src.external_api.requests.request")
def test_amount_transaction_other_currency(mock_request: Any) -> None:
    """Проверяем, что транзакция в другой валюте корректно обрабатывается"""
    mock_request.return_value.json.return_value = {"result": 735306.260822}
    transaction: Dict[str, Any] = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"name": "USD", "code": "USD"},
        },
    }
    result: float = amount_transaction(transaction)
    assert result == 735306.260822
    mock_request.assert_called_once()


if __name__ == "__main__":
    unittest.main()
