import datetime
from functools import wraps


def wrong_timelogger(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(func.__name__, end_time - start_time)
        return result
    return wrapper


def timelogger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(func.__name__, end_time - start_time)
        return result
    return wrapper


@timelogger
def loop(num: int) -> None:
    """
    :param num:
    :return:
    """
    while num > 0:
        num -= 1


loop(100000000)
print(loop.__name__)
print(loop.__doc__)
print(loop.__annotations__)


