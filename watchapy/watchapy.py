from typing import Callable
from functools import wraps

def watchapy(enable: bool=True):
    def watchapy_decorator(func: Callable):
        if enable:
            print(f'watching {func.__name__}')

            @wraps(func)
            def apywatcher(*args, **kwargs):
                print(f'calling {func.__name__}')
                result = func(*args, **kwargs)
                print(f'called {func.__name__}')
                return result
            return apywatcher
        else:
            return func


    return watchapy_decorator
