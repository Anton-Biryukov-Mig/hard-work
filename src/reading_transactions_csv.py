import csv
import logging
import os
from typing import Any, Dict, List

import pandas as pd

from config import DATA_DIR, LOGS_DIR

logger = logging.getLogger(__name__)
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

file_handler = logging.FileHandler(os.path.join(LOGS_DIR, f"{__name__}.log"), mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_data_transactions(operations_path: str) -> List[Dict[str, Any]]:
    """функция возвращает список словарей с данными о  транзакциях"""
    try:
        logger.info("открытие файла transactions.csv")
        with open(operations_path, encoding="utf-8") as f:
            try:
                logger.info("Получение информации о транзакциях")
                reader = pd.read_csv(f, delimiter=";")
                dict_trans = reader.to_dict(orient="records")

                # преобразование словарей в словари с числовыми ключами
                dict_trans_str_keys = [{str(k): v for k, v in d.items()} for d in dict_trans]

            except csv.Error as e:
                logger.error(f"Ошибка чтения CSV файла: {e}")
                return []

    except FileNotFoundError:
        logger.error("путь к файлу transactions.csv не найден")
        return []

    return dict_trans_str_keys


if __name__ == "__main__":
    operations_path = os.path.join(DATA_DIR, "transactions.csv")
    list_trans = get_data_transactions(operations_path)
    print(type(list_trans))
    print(*list_trans, sep="\n")
