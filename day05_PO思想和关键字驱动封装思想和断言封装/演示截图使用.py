
from playwright.sync_api import Page,expect



from pageobjects.page_login import LoginPage
from pageobjects.page_home import HomePage





def test_homework(page:Page):
    #打开页面
    page.goto("http://mall.lemonban.com:3344/")

    #home 操作页类
    home_page = HomePage(page)

    #登录操作类
    loginpage = LoginPage(page)


    #订单流程
    #点击登录
    home_page.click_login()

    #输入账号密码
    loginpage.aconunt_login("lemon_auto","lemon123456")


    page.screenshot(path="./screenshot.png")

    page.screenshot(path="screenshot01.png",full_page=True)

    page.locator('//span[text() = "欢迎来到柠檬班"]').screenshot(path="lemon.png")
