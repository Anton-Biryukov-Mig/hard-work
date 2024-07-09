from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """Функция принимает на вход список словарей и значение для ключа state."""
    filtered_data = [{"state": d["state"], "date": d["date"]} for d in data if d["state"] == state]
    return filtered_data


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает на вход список словарей и возвращает новый список."""
    return sorted(data, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse)
