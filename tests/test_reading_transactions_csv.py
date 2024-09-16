import logging
import os
import unittest
from typing import Any, Dict, List

import pandas as pd

from src.reading_transactions_csv import get_data_transactions


class TestReadingTransactionsCSV(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_path: str = ""
        self.data: List[Dict[str, Any]] = []

    def test_get_data_transactions(self) -> None:
        assert isinstance(self.csv_path, str)
        try:
            pd.read_csv(self.csv_path, sep=";")
            logging.info("Получение информации о транзакциях")
        except FileNotFoundError:
            logging.error(f"Путь к файлу {self.csv_path} не найден")

    def test_get_data_transactions_existing_file(self) -> None:
        """Тестирование чтения существующего файла"""
        self.data = [
            {"id": 1, "state": "EXECUTED", "amount": 100},
            {"id": 2, "state": "PENDING", "amount": 200},
            {"id": 3, "state": "CANCELED", "amount": 300},
        ]
        self.csv_path = "test_transactions_csv"
        pd.DataFrame(self.data).to_csv(self.csv_path, sep=";", index=False)
        result = get_data_transactions(self.csv_path)
        assert isinstance(result, list)
        assert all(isinstance(item, dict) for item in result)
        assert len(result) == len(self.data)
        for i, transaction in enumerate(result):
            assert transaction["id"] == self.data[i]["id"]
            assert transaction["state"] == self.data[i]["state"]
            assert transaction["amount"] == self.data[i]["amount"]

    def test_get_data_transactions_invalid_csv(self) -> None:
        """Тестирование обработки ошибки при некорректном CSV"""
        self.data = [
            {"id": 1, "state": "EXECUTED", "amount": 100},
            {"id": 2, "state": "PENDING", "amount": 200},
            {"id": 3, "state": "CANCELED", "amount": 300},
        ]
        invalid_csv_path = "invalid_transactions.csv"
        with open(invalid_csv_path, "w", encoding="utf-8") as f:
            f.write("id;state;amount\n")

        result = get_data_transactions(invalid_csv_path)
        assert isinstance(result, list)
        assert len(result) == 0
        os.remove(invalid_csv_path)

    def test_get_data_transactions_nonexistent_file(self) -> None:
        """Тестирование обработки ошибки при отсутствии файла"""
        result = get_data_transactions("nonexistent_file.csv")
        assert isinstance(result, list)
        assert len(result) == 0


if __name__ == "__main__":
    unittest.main()
