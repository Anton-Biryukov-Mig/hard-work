from masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str | None:
    """Функция общей маскировки карты и счета"""
    if "Visa Platinum" in input_string or "Maestro" in input_string:
        return get_mask_card_number(input_string)
    elif "Счет" in input_string:
        return get_mask_account(input_string)
    else:
        return


def get_data(input_string: str) -> str | None:
    """Функция преобразования даты"""
    date = input_string.split("T")[0]
    formatted_date = f"{date[-2:]}.{date[5:7]}.{date[:4]}"
    return formatted_date
