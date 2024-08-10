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


def get_data_transactions(path: str) -> List[Dict[str, Any]]:
    """Функция возвращает список словарей с данными о транзакциях"""
    try:
        logger.info("Открытие файла %s", path)
        with open(path, encoding="utf-8") as f:
            try:
                logger.info("Получение информации о транзакциях %s", path)
                data_transactions: List[Dict[str, Any]] = json.load(f)
            except json.JSONDecodeError:
                logger.error("Невозможно декодировать файл %s", path)
                return []
    except FileNotFoundError:
        logger.error("Путь к файлу %s не найден", path)
        return []
    return data_transactions


if __name__ == "__main__":
    path = "../data/operations.json"
    list_trans = get_data_transactions(path)
    print(type(list_trans))
    print(*list_trans, sep="\n")
