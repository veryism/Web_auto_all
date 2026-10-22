


#conftest.py

import pytest

import allure
from pygments.styles import default


#hook 函数是每条测试用例执行完的时候调用找个方法,他类似一个钩子函数有在用例执行前来执行了
#测试用例执行完来执行判断用例失败的进行截图
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    #获取到每条测试的结果，保存到变量reprot 中
    outcome = yield
    report = outcome.get_result()

    #判断用例是否是为失败
    if report.when == 'call' and report.failed:
        #获取到页面对象
        page = item.funcargs.get("page",None)

        #判断是否获取到页面对象
        if page:
            #页面对象不为空，获取当前页面截图
            screenshot = page.screenshot()
            #将截图插入到 allure 报告当中
            allure.attach(
                screenshot,
                name=f"{item.name}_失败截图",
                attachment_type = allure.attachment_type.PNG
            )


#设置在执行前获取参数
def pytest_addoption(parser):
    parser.addoption(
        "--env-url",
        default="http://mall.lemonban.com:3344/",
        choices=["http://mall.lemonban.com:3344/","http://mall.dev.lemonban.com:3344/","http://mall.test.lemonban.com:3344/"],
        help="选择运行环境"
    )


@pytest.fixture
def get_env_url(request):
    return request.config.getoption("--env-url")