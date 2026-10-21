

from playwright.sync_api import sync_playwright, Page


def test_login(page:Page):

    page.goto("http://shop.lemonban.com:3344/")

    #点击登录按钮
    page.locator('//a[text()="登录"]').click()

    #输入账号密码
    page.locator('//input[@placeholder="请输入手机号/用户名"]').fill("lemon_auto")
    page.locator('//input[@placeholder="请输入密码"]').fill("lemon123456")

    #点击登录按钮

    page.locator('//a[text()="登录" and @class="login-button"]').click()

    print("title:",page.title())
    print("title:",type(page.title()))


