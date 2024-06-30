def get_mask_card_number(card_info: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    card_info = card_info.replace(" ", "")
    for i in range(len(card_info)):
        if card_info[i].isdigit():
            index = i
            break

    card_type = card_info[:index]
    card_number = card_info[index:]
    if len(card_number) != 16:
        return "Неверный формат входных данных"

    masked_number = card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return card_type + " " + masked_number


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"Счет **{account_number[-4:]}"

