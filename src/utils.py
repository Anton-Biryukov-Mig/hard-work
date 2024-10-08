import json
import logging
import os
from typing import Any, Dict, List

logger = logging.getLogger(__name__)
project_dir = os.path.dirname(os.path.dirname(__file__))
logs_dir = os.path.join(project_dir, "logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

file_handler = logging.FileHandler(os.path.join(logs_dir, f"{__name__}.log"), mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

DATA_DIR = os.path.dirname(os.path.dirname(__file__))
OPERATIONS_FILE = os.path.join(DATA_DIR, "data", "operations.json")


def get_data_transactions(operations_path: str) -> List[Dict[str, Any]]:
    """Функция возвращает список словарей с данными о транзакциях"""

    try:
        logger.info("открытие файла operations.json")
        with open(operations_path, "r", encoding="utf-8") as file:
            logger.info("Получение информации о транзакциях")
            data_transactions: List[Dict[str, Any]] = json.load(file)
        return data_transactions
    except (json.JSONDecodeError, FileNotFoundError):
        logger.info("открытие файла operations.json")
        return []


if __name__ == "__main__":
    operations_path = "../data/operations.json"
    list_trans = get_data_transactions(operations_path)
    print(type(list_trans))
    print(*list_trans, sep="\n")
