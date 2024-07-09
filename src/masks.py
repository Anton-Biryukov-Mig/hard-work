import re


def get_mask_card_number(card_info: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    card_info = card_info.replace(" ", "")
    enumeration = None
    for i, char in enumerate(card_info):
        if char.isdigit():
            enumeration = i
            break

    if enumeration is None:
        return "Неверный формат входных данных"

    card_type, card_number = card_info[:enumeration], card_info[enumeration:]
    if len(card_number) != 16:
        return "Неверный формат входных данных"

    card_type_with_spaces = re.sub(r"([A-Z])", r" \1", card_type).strip()
    masked_number = card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return f"{card_type_with_spaces} {masked_number}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return "Счет **" + account_number[-4:]

