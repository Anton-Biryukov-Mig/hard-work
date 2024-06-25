def get_mask_card_number(card_number: str) -> str | None:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    masked_number = card_number[:21] + "** **** " + card_number[-4:]
    return masked_number


def get_mask_account(account_number: str) -> str | None:
    """Функция принимает на вход номер счета и возвращает его маску"""
    masked_number = account_number[:5] + "**" + account_number[-4:]
    return masked_number
