from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str) -> List[Dict[str, Any]]:
    """Функция принимает на вход список словарей и значение для ключа state."""
    return [item for item in data if item.get("state") == state]



def sort_by_date(data: List[Dict[str, Any]], reverse: bool = False) -> List[Dict[str, Any]]:
    """Функция принимает на вход список словарей и возвращает новый список."""
    return sorted(data, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse)
