from typing import Dict, List, Any
from unittest.mock import mock_open, patch

from src.utils import get_data_transactions


def test_successful_read() -> None:
    """проверяем, что файл json корректно читается"""
    mock_data = (
        '[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount": '
        '{"amount": "31957.58", "currency": '
        '{"name": "руб.", "code": "RUB"}}}]'
    )
    with patch("builtins.open", mock_open(read_data=mock_data)):
        data: List[Dict[str, Any]] = get_data_transactions("path_to_file.json")
        assert data == [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {"name": "руб.", "code": "RUB"},
                },
            }
        ]
        print("test_successful_read")


def test_file_not_found() -> None:
    """проверяем ответ, при некорректном пути к файлу json"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        data: List[Dict[str, Any]] = get_data_transactions("non_path_file.json")
        assert data == []
        print("test_file_not_found")


def test_json_decode_error() -> None:
    """проверяем ответ, при некорректном json файле"""
    mock_data = (
        '[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount": '
        '{"amount": "31957.58", "currency": '
    )
    with patch("builtins.open", mock_open(read_data=mock_data)):
        data: List[Dict[str, Any]] = get_data_transactions("uncorrect_file.json")
        assert data == []
        print("test_json_decode_error")
