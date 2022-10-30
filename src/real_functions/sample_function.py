import warnings


def hello():
    return "hello world"


def dummy_function():
    # This is the desired function we are testing
    return hello()


def add_number(x: int, y: int):
    return x + y


class FunctionGroup:

    def __init__(self):
        self.feature_one = "one"
        self.feature_two = "two"

    def function_one(self):
        return self.feature_one

    def function_two(self):
        return self.feature_two


def api_v1():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    return 1


def api_v2():
    warnings.warn(UserWarning("warning label, should use functions from v1"))
    return 1
