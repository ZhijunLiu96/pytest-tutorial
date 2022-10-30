# require pip install pytest-mock
from src.real_functions import sample_function


def test_hello_function():
    assert sample_function.hello() == "hello world"


def test_mocking_function(mocker):
    mocker.patch("src.real_functions.sample_function.hello", return_value="hello")
    assert sample_function.dummy_function() == "hello", "Value should be mocked"


def test_mocking_function_2(mocker):
    hello_mocker = mocker.patch("src.real_functions.sample_function.hello")
    hello_mocker.return_value = "hello"
    assert sample_function.dummy_function() == "hello", "Value should be mocked"


def test_patch_obj(mocker):
    object_mocker = mocker.patch.object(sample_function.FunctionGroup, "function_one")
    object_mocker.return_value = "mock function 1"
    test_example = sample_function.FunctionGroup()
    assert test_example.function_one() == "mock function 1"


foo = {}


def test_patch_dict(mocker):
    mocker.patch.dict(foo, {'newkey': 'newvalue'})
    assert foo == {'newkey': 'newvalue'}
