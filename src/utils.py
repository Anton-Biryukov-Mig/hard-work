import json
import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    "C:/Projects/FirstPython/my_prj/anton_biryukov_home_work/logs/utils.log", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_data_transactions(path: str) -> List[Dict[str, Any]]:
    """Функция возвращает список словарей с данными о транзакциях"""
    try:
        logger.info("Открытие файла operations.json")
        with open(path, encoding="utf-8") as f:
            try:
                logger.info("Получение информации о транзакциях")
                data_transactions: List[Dict[str, Any]] = json.load(f)
            except json.JSONDecodeError:
                logger.error("Невозможно декодировать файл operations.json")
                return []
    except FileNotFoundError:
        logger.error("Путь к файлу operations.json не найден")
        return []
    return data_transactions


if __name__ == "__main__":
    path = "C:/Projects/FirstPython/my_prj/anton_biryukov_home_work/data/operations.json"
    list_trans = get_data_transactions(path)
    # n = int(input("введите количество транзакций: "))
    # for i in range(n):
    #     print(list_trans[i])
    print(type(list_trans))
    print(*list_trans, sep="\n")
