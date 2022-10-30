import pytest


# @pytest.fixture(scope="class")
@pytest.fixture
def order():
    return []


@pytest.fixture
def update(order):
    def _update(info):
        order.append(info)
    return _update


class TestOne:

    def test_order_one(self, order, update):
        update("one")
        assert order == ["one"]

    def test_order_two(self, order, update):
        update("one")
        update("two")
        assert order == ["one", "two"]

    def test_order_three(self, order, update):
        update("three")
        assert order == ["three"]


@pytest.fixture(scope="class")
def file_system(request):
    request.cls.file_system = []


@pytest.mark.usefixtures("file_system")
class TestThree:

    def test_download_camera(self):
        self.file_system.append("camera")
        assert self.file_system == ["camera"]

    def test_download_bin_false(self):
        self.file_system.append("bin")
        assert self.file_system == ["camera", "bin"]

    def test_download_parameters_true(self):
        self.file_system.append("parameters")
        assert self.file_system == ["camera", "bin", "parameters"]


class TestFour:

    def test_download_camera(self, file_system):
        self.file_system.append("camera")
        assert self.file_system == ["camera"]

    def test_download_bin_false(self, file_system):
        self.file_system.append("bin")
        assert self.file_system == ["camera", "bin"]

    def test_download_parameters_true(self, file_system):
        self.file_system.append("parameters")
        assert self.file_system == ["camera", "bin", "parameters"]


# @pytest.fixture(scope="class", autouse=True)
# def file_system(request):
#     request.cls.file_system = []
#
#
# class TestFive:
#
#     def test_download_camera(self):
#         self.file_system.append("camera")
#         assert self.file_system == ["camera"]  # pass
#
#     def test_download_bin_false(self):
#         self.file_system.append("bin")
#         assert self.file_system == ["camera"]  # fail
#
#     def test_download_parameters_true(self):
#         self.file_system.append("parameters")
#         assert self.file_system == ["camera", "bin", "parameters"]  # pass


@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return [name]

    return _make_customer_record


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")  # ["Lisa"]
    customer_2 = make_customer_record("Mike")  # ["Mike"]
    customer_3 = make_customer_record("Meredith")  # ["Meredith"]
    assert customer_3 == ["Meredith"]
