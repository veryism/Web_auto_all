import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://mall.lemonban.com:3344/")
    page.get_by_role("link", name="登录").click()
    page.get_by_role("textbox", name="请输入手机号/用户名").click()
    page.get_by_role("textbox", name="请输入手机号/用户名").fill("lemon_auto")
    page.get_by_role("textbox", name="请输入密码").click()
    page.get_by_role("textbox", name="请输入密码").fill("lemon123456")
    page.get_by_role("link", name="登录").nth(1).click()

    page.wait_for_timeout(4000)
    page.get_by_role("textbox", name="请输入商品名称").click()
    page.get_by_role("textbox", name="请输入商品名称").fill("包")
    page.get_by_role("button", name="搜索").click()
    page.wait_for_timeout(4000)

    page.locator("div:nth-child(2) > .goods-testdatas > testdatas").click()
    page.get_by_role("link", name="立即购买").click()
    page.wait_for_timeout(4000)
    page.get_by_role("link", name="提交订单").click()
    page.get_by_text("微信支付").click()
    page.get_by_role("link", name="立即付款").click()
