import time

import pytest

# from test_homework2.test_calc import Calculator

@pytest.fixture(autouse=True)
def start_info():
    print("开始计算")
    yield
    print("结束计算")

@pytest.fixture(scope="session",autouse=True)
def end_info():
    pass
    yield
    print("测试结束")

@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""

    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_name = './logs/' + now + '.log'
    request.config.pluginmanager.get_plugin("logging-plugin").set_log_path(log_name)

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")