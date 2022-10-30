import pytest

from src.real_functions import sample_function


# def test_filterwarnings_one():
#     assert sample_function.api_v1() == 1


@pytest.mark.filterwarnings("ignore:api v1")
def test_filterwarnings_two():
    assert sample_function.api_v1() == 1


@pytest.mark.filterwarnings("ignore:warning label")
def test_filterwarnings_three():
    assert sample_function.api_v2() == 1


@pytest.mark.filterwarnings("error")
def test_filterwarnings_four():
    assert sample_function.api_v1() == 1


@pytest.mark.skip
def test_skip_one():
    assert sample_function.hello() == "hello world"


condition = 1


@pytest.mark.skipif(condition == 0, reason="test build-in marker")
def test_skip_two():
    assert sample_function.hello() == "hello world"


@pytest.mark.skipif(condition == 1, reason="test build-in marker")
def test_skip_three():
    assert sample_function.hello() == "hello world"


@pytest.mark.xfail(condition == 1, reason="bug in a 3rd party library")
def test_xfail_one():
    assert 1 == 0


@pytest.mark.xfail(condition == 1, reason="bug in a 3rd party library", strict=False)
def test_xfail_two():  # xpass
    assert 1 == 1


@pytest.mark.xfail(condition == 1, reason="bug in a 3rd party library", strict=True)
def test_xfail_three():  # fail
    assert 1 == 1


@pytest.mark.xfail(condition == 0, reason="bug in a 3rd party library")
def test_xfail_four():
    assert 1 == 1


@pytest.mark.xfail(raises=RuntimeError)
def test_xfail_five():
    raise Exception


@pytest.mark.xfail(raises=RuntimeError)
def test_xfail_six():
    raise RuntimeError


@pytest.mark.parametrize("x,y,expected", [(1, 1, 2), (2, 2, 4), (3, 3, 6)])
def test_parametrize(x: int, y: int, expected: int):
    assert sample_function.add_number(x, y) == expected


@pytest.mark.group1
def test_group_1():
    assert 1 == 1


@pytest.mark.group1
def test_group_2():
    assert 1 == 1


@pytest.mark.group1
def test_group_3():
    assert 1 == 1


@pytest.mark.group1
def test_group_4():
    assert 1 == 1
