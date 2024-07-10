# Учебный проект по Python
#   d e v e l o p 
 
## Тестирование

Для проверки работоспособности функционала проекта реализованы тесты с использованием библиотеки pytest. Ниже приведены некоторые кейсы тестирования:

### Функция get_mask_card_number:
- `test_get_mask_card_number`: тест проверяет корректность маскирования номеров карт.

### Функция get_mask_account:
- `test_get_mask_account`: проверяет правильность маскирования номеров счетов.

### Функция mask_account_card:
- Тесты на проверку маскирования номеров карт.

### Функция get_data:
- Проверка преобразования даты из формата UTC в день.месяц.год.

### Функции filter_by_state и sort_by_date:
- Тест проверки фильтрации транзакций по состоянию и сортировки по дате.

### Функция filter_by_currency:
- Тест проверки как принимает на вход список словарей, представляющих транзакции.

### Функция transaction_descriptions:
- Тест проверки списка словарей с транзакциями и как возвращает описание каждой операции по очереди.

### Функция card_number_generator:
- Тест проверки как выдает номера банковских карт и соответствие формату XXXX XXXX XXXX XXXX.


