import logging
import time
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Декоратор log автоматически логирует начало и конец выполнения функции и результаты или возникшие ошибки"""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                execution_time = end_time - start_time
                log_message = (
                    f"{func.__name__} ok. Execution time: {execution_time:.2f} seconds. "
                    f"Inputs: {args}, Result: {result}"
                )
                if filename:
                    logging.basicConfig(filename=filename, level=logging.INFO)
                    logging.info(log_message)
                else:
                    print(log_message)
                return result
            except Exception as e:
                end_time = time.time()
                execution_time = end_time - start_time
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}. Error: {str(e)}"
                if filename:
                    logging.basicConfig(filename=filename, level=logging.ERROR)
                    logging.error(log_message)
                else:
                    print(log_message)
                raise

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
