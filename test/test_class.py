from src.real_functions import sample_function


class TestClass:  # Prefix class with Test
    def test_one(self):  # prefix function with test_
        total = sample_function.add_number(x=1, y=1)
        assert total == 2

    def test_two(self):  # prefix function with test_
        total = sample_function.add_number(x=2, y=2)
        assert total == 4

    def add_num_three(self):  # skipped
        total = sample_function.add_number(x=3, y=3)
        assert total == 6


class SkipClass:  # skipped
    def test_one(self):
        total = sample_function.add_number(x=1, y=1)
        assert total == 2

    def test_two(self):
        total = sample_function.add_number(x=2, y=2)
        assert total == 4
