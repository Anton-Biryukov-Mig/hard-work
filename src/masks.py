def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    parts = card_number.split()
    if len(parts) != 6 or not all(part.isdigit() for part in parts[2:]):
        return "Неверный формат номера карты"
    masked_parts = parts[:3] + [parts[3][:2] + "**"] + ["****"] + [parts[5]]
    return " ".join(masked_parts)


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"Счет **{account_number[-4:]}"
