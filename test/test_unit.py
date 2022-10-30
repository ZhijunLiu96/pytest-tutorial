import time

from src.real_functions import sample_function


def test_hello():
    time.sleep(2)
    assert sample_function.hello() == "hello world"


def test_add_number():
    assert sample_function.add_number(x=1, y=2) == 3


def hello_test():
    assert sample_function.hello() == "hello world"
