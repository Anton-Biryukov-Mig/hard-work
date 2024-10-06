import logging
import os
from typing import Any

from config import DATA_DIR, LOGS_DIR
from utils import get_data_transactions

logger = logging.getLogger(__name__)
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

file_handler = logging.FileHandler(os.path.join(LOGS_DIR, f"{__name__}.log"), mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def currency_cod_transaction(transactions: list[dict[str, Any]], currency_cod: str) -> list[dict[str, Any]] | str:
    """вывод транзакции, содержащей заданную валюту"""

    logger.info("поиск транзакции, содержащей заданную валюту")
    try:
        my_transactions = []
        for transaction in transactions:
            try:
                if "operationAmount" in transaction:
                    if transaction["operationAmount"]["currency"]["code"] == currency_cod:
                        logger.info("данный файл изначально был в формате JSON")
                        my_transactions.append(transaction)
                elif "currency_code" in transaction:
                    if transaction["currency_code"] == currency_cod:
                        logger.info("данный файл изначально  не был в формате JSON")
                        my_transactions.append(transaction)
                else:
                    logger.warning(f"Транзакция без нужных ключей: {transaction}")
            except Exception as e:
                logger.error(f"Неожиданная ошибка: {e} в транзакции: {transaction}")

        if my_transactions:
            return my_transactions
        else:
            return "Транзакций с такой валютой нет"

    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return "Произошла ошибка при поиске валюты транзакции"


if __name__ == "__main__":
    operations_path = os.path.join(DATA_DIR, "operations.json")
    list_trans = get_data_transactions(operations_path)

    my_currency_cod = input("введите валюту транзакции RUB, USD, EUR: ")
    result = currency_cod_transaction(list_trans, my_currency_cod)
    if isinstance(result, str):
        print(result)
    else:
        print(*result, sep="\n")
