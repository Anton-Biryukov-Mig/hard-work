from datetime import datetime
from typing import Any, Dict, List, Union


def filter_by_state(data: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, Union[str, None]]]:
    """Функция принимает на вход список словарей и значение для ключа state."""
    filtered_data = [{"state": d.get("state"), "date": d.get("date")} for d in data if d.get("state") == state]
    return filtered_data


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает на вход список словарей и возвращает новый список."""
    def parse_date(date_string):
        return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")

    return sorted(data, key=lambda x: parse_date(x["date"]), reverse=reverse)
