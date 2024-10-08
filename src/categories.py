import logging
import os
from collections import Counter
from typing import Any, Dict, List

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


def list_categories(transactions: List[Dict[str, Any]]) -> Dict[str, int]:
    """Функция подсчёта операций по категориям"""
    categories = [transaction["description"] for transaction in transactions if "description" in transaction]
    return dict(Counter(categories))


def categories_by_descriptions() -> Dict[str, int]:
    list_trans = get_data_transactions(operations_path)
    if list_trans is None:
        return Counter()

    my_list_categories = list_categories(list_trans)
    return Counter(my_list_categories)


if __name__ == "__main__":
    operations_path = os.path.join(DATA_DIR, "operations.json")
    get_data_transactions(operations_path)
    print(categories_by_descriptions())
