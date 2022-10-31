# Pytest


## Command

```shell
pytest

pytest test/

pytest test/test_unit.py 

pytest test/test_unit.py::test_hello

pytest test/test_class.py::TestClass

pytest test/test_class.py::TestClass::test_one

pytest test/test_unit.py --durations=10 --durations-min=1.0
pytest test/test_unit.py --durations=10 --durations-min=1.0 -vv

pytest --runxfail  # ignore xfail

pytest -m "not group1"

pytest -m group1

pytest -k unit # matching filename keyword)

pytest --report-log=./testlog.log test/ # log output to file pip install pytest-reportlog

pytest --cov=./src test/  # pytest --cov=myproj tests/
```

## How to write test class/function

```shell
pytest test/test_unit.py
pytest test/unit_test.py
pytest test/test_class.py
```

## [Marker](https://docs.pytest.org/en/7.1.x/how-to/mark.html#mark)

Mark test functions with attributes

```txt
[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    serial
```

Here are some of the builtin markers:

- usefixtures - use fixtures on a test function or class

- filterwarnings - filter certain warnings of a test function

- skip - always skip a test function

- skipif - skip a test function if a certain condition is met

- xfail - produce an “expected failure” outcome if a certain condition is met

- parametrize - perform multiple calls to the same test function.

```shell
pytest test/test_marker.py
pytest test/test_marker.py -m group1
pytest test/test_marker.py -m "not group1"
```

## [Fixture](https://docs.pytest.org/en/7.1.x/reference/fixtures.html#fixtures)


scope

- func (default)
- cls
- mod
- pack
- ...

autouse: to be implemented

- https://docs.pytest.org/en/7.1.x/how-to/fixtures.html#fixture-parametrize

```shell
pytest test/test_fixture.py::TestOne

pytest test/test_fixture.py::TestThree

pytest test/test_fixture.py::TestFour

# turn on/off auto use
pytest test/test_fixture.py::TestFive
pytest test/test_fixture.py::test_customer_records
```

## [Monkeypatch](https://docs.pytest.org/en/7.1.x/how-to/monkeypatch.html?highlight=mock)

- setenv
- delenv
- setattr
- delattr
- setitem
- delitem

```shell
pytest test/test_monkeypatch.py
```


## [Mock](https://pytest-mock.readthedocs.io/en/latest/usage.html)

- mocker.patch
- mocker.patch.object
- mocker.patch.dict

```shell
pytest test/test_mock.py
```
