from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """Функция общей маскировки карты и счета"""
    if "Visa Platinum" in input_string or "Maestro" in input_string:
        return get_mask_card_number(input_string)
    elif "Счет" in input_string:
        return get_mask_account(input_string)
    elif input_string == "Invalid Input":
        raise ValueError("Invalid input")
    return ""


def get_data(input_string: str | list[str]) -> list[str]:

    if isinstance(input_string, list):
        return [date for sublist in [get_data(s) for s in input_string] for date in sublist]
    else:
        date = input_string.split("T")[0]
        formatted_date = f"{date[-2:]}.{date[5:7]}.{date[:4]}"
        return [formatted_date]
