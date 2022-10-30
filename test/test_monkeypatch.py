import os
import types

import pytest

from src.real_functions import sample_function


def test_update_env(monkeypatch):
    monkeypatch.setenv('pytest_env', 'dev')
    assert os.getenv("pytest_env") == 'dev'


def test_del_env(monkeypatch):
    assert os.getenv("USER") is not None
    monkeypatch.delenv('USER')
    assert os.getenv("USER") is None


def test_monkeypatch_setattr_example_one(monkeypatch):
    example_obj = sample_function.FunctionGroup()
    monkeypatch.setattr(example_obj, "feature_one", 1)
    assert example_obj.feature_one == 1


def test_monkeypatch_setattr_example_two(monkeypatch):
    example_obj = sample_function.FunctionGroup()

    def mock_feature_one():
        return "feature one"

    monkeypatch.setattr(example_obj, "function_one", mock_feature_one)
    assert example_obj.function_one() == "feature one"


def test_monkeypatch_setattr_example_three(monkeypatch):
    example_obj = sample_function.FunctionGroup()

    def mock_feature_one(*args):
        self = args[0]
        return "feature " + self.feature_one

    monkeypatch.setattr(example_obj, "function_one", types.MethodType(mock_feature_one, example_obj))
    assert example_obj.function_one() == "feature one"


def test_monkeypatch_delattr_example_one(monkeypatch):
    example_obj = sample_function.FunctionGroup()
    monkeypatch.delattr(example_obj, "feature_one")
    # assert example_obj.feature_one == "one"
    with pytest.raises(AttributeError):
        assert example_obj.feature_one == "one"


dictionary_example = {"a": 1, "b": 2}


def test_monkeypatch_setitem_example(monkeypatch):
    monkeypatch.setitem(dictionary_example, "c", 3)
    assert dictionary_example["c"] == 3


def test_monkeypatch_delitem_example(monkeypatch):
    monkeypatch.delitem(dictionary_example, "b")
    assert "b" not in dictionary_example
