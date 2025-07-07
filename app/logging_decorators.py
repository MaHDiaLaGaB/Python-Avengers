import logging
import input


logging.basicConfig(
        level=logging.DEBUG,
        filename="my_app.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="a"
                    )


def sign_up(name):
    logging.info(f"we just start logging the user {name}")
    logging.debug(f"lets close the function")
    logging.warning(f"this is warning")
    logging.error("this is error")


def decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"this is the function name we called {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@decorator
def say_hi():
    print("lets start ..... 1 2 3")

say_hi()


