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
    """Функция получения информации о транзакциях из XLSX-файла"""
    logger = logging.getLogger(__name__)
    try:
        df = pd.read_excel(operations_path)
        logger.info(f"открытие файла {operations_path}")
        logger.info("Получение информации о транзакциях")
        dict_trans = df.to_dict(orient="records")

        # Convert keys to strings
        dict_trans_str_keys = [{str(k): v for k, v in d.items()} for d in dict_trans]

        return dict_trans_str_keys
    except FileNotFoundError:
        logger.error(f"путь к файлу {operations_path} не найден")
        return []
    except ValueError as e:
        logger.error(f"Ошибка при парсинге Excel файла: {str(e)}")
        return []


if __name__ == "__main__":
    operations_path = os.path.join(DATA_DIR, "transactions_excel.xlsx")
    list_trans = get_data_transactions(operations_path)
    print(type(list_trans))
    print(*list_trans, sep="\n")
