import logging
import re

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    "C:/Projects/FirstPython/my_prj/anton_biryukov_home_work/logs/masks.log", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(card_info: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logger.info("маскируем банковскую карту клиента")
    card_info = str(card_info).replace(" ", "")
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
    logger.info("маскируем банковский счет клиента")
    return "Счет **" + account_number[-4:]


if __name__ == "__main__":
    print(get_mask_card_number("Maestro 1596837868705199"))
    print(get_mask_account("64686473678894779589"))
