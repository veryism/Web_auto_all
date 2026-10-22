import pytest
from playwright.sync_api import Page,expect
from pyexpat import expat_CAPI
from urllib3.util import timeout

from pageobjects import page_home
from pageobjects import page_login
from loguru import logger


def test_update_porf(page:Page,get_env_url):

    logger.info(f"访问的环境链接:{get_env_url}")

    page.goto(get_env_url)

    # 实例化类

    #主页面类实例化
    home_page = page_home.HomePage(page)


    #点击登录 按钮
    home_page.click_login()
    #输入 账号密码
    page_login.LoginPage(page).aconunt_login(username="lemon_auto", password="lemon123456")

    expect(home_page.is_welcome_tips_locator()).to_be_visible()

    expect(home_page.is_username_locator()).to_have_text("lemon_auto")


#没有使用数据驱动代码

# def test_update_account_lens_4(page: Page):
#
#
#     logger.info("验证账号输入不符合预期的长度")
#     page.goto('http://mall.lemonban.com:3344/')
#
#     # 实例化类
#     # 主页面类实例化
#     home_page = page_home.HomePage(page)
#
#     # 点击登录 按钮
#     home_page.click_login()
#
#     login_page = page_login.LoginPage(page)
#     # 输入 账号密码
#     login_page.aconunt_login(username="leo", password="lemon123456")
#
#     expect(login_page.is_aconnut_errot_tips_locator()).to_be_visible()
#
#
#
# def test_update_account_morethan_16(page: Page):
#
#     logger.info("验证账号输入不符合预期的长度")
#     page.goto('http://mall.lemonban.com:3344/')
#
#     # 主页面类实例化
#     home_page = page_home.HomePage(page)
#
#     # 点击登录 按钮
#     home_page.click_login()
#
#     login_page = page_login.LoginPage(page)
#     # 输入 账号密码
#     login_page.aconunt_login(username="lemon_autolemon_autolemon_auto", password="lemon123456")
#
#     expect(login_page.is_aconnut_errot_tips_locator()).to_be_visible()




# 使用数据驱动的账号密码测试

test_datas = [
    {"username": "leo", "password": "lemon123456"},
    {"username": "lemon_autolemon_autolemon_auto", "password": "lemon123456"},
    {"username": "lemon_#$%@", "password": "lemon123456"},
]



@pytest.mark.parametrize("test_data", test_datas)
def test_update_account_lenth_limit(page: Page,test_data,get_env_url):

    logger.info("验证账号密码输入不符合预期的长度4-16")
    page.goto(get_env_url)
    # 实例化类
    # 主页面类实例化
    home_page = page_home.HomePage(page)

    # 点击登录 按钮
    home_page.click_login()

    login_page = page_login.LoginPage(page)
    # 输入 账号密码
    login_page.aconunt_login(username=test_data["username"], password=test_data["password"])

    expect(login_page.is_aconnut_errot_tips_locator()).to_be_visible()

# 如果不是和上面一样的检查断言,就不能加入数据驱动数据中


def test_update_account_password_error(page: Page,get_env_url):

    logger.info("输入的账号密码不匹配")
    page.goto(get_env_url)
    # 实例化类
    # 主页面类实例化
    home_page = page_home.HomePage(page)

    # 点击登录 按钮
    home_page.click_login()

    login_page = page_login.LoginPage(page)
    # 输入 账号密码
    login_page.aconunt_login(username="lemon_autole", password="lemon123456")

    expect(login_page.is_acoont_password_error_tips()).to_be_visible()