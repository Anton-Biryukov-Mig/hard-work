import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

from src.utils import get_data_transactions

load_dotenv("../.env")

operations_path = "../data/operations.json"


def amount_transaction(transaction_by_id: Dict[str, Any]) -> float:
    """Функция возвращает сумму транзакции в рублях"""
    trans_amount = transaction_by_id["operationAmount"]["amount"]
    trans_code = transaction_by_id["operationAmount"]["currency"]["code"]
    api_key = os.getenv("API_KEY")
    headers_api = {"apikey": api_key}
    if trans_code == "RUB":
        return float(trans_amount)
    else:
        try:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={trans_code}&amount={trans_amount}"
            response = requests.request("GET", url, headers=headers_api)
            my_result = response.json()
            return float(my_result["result"])
        except Exception as e:
            print(e)
            return 0.0  # Default return value in case of an exception


if __name__ == "__main__":
    operations_path = "../data/operations.json"
    transactions = get_data_transactions(operations_path)
    n = int(input("введите колличество транзакций: "))
    for i in range(n):
        print(amount_transaction(transactions[i]))
