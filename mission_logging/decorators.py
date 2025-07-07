# decorators.py
from ... import ...
from functools import wraps

def log_mission(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # TODO finish the decoratore
        ...
    return wrapper
